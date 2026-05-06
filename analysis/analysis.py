"""
Visual Search Midterm Project — Analysis Script
================================================
Analyses pilot data collected on Pavlovia for a feature-vs-conjunction
visual search experiment with set sizes 4, 12, 24.

Inputs : ../data/<participant>_midterm_project_*.csv  (PsychoPy CSV output)
Outputs: ../figures/rt_by_setsize_condition.png
         ../figures/accuracy_by_setsize_condition.png
         ../figures/search_slopes.png

Run from the analysis/ directory:
    python analysis.py
"""

from pathlib import Path
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
FIG_DIR = HERE.parent / "figures"
FIG_DIR.mkdir(exist_ok=True)

RT_LOWER, RT_UPPER = 0.10, 1.50

INCLUDED_PIDS = {"098713", "1", "2", "3", "4", "5", "808749", "190332"}


def load_participant(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df = df[df["formal_loop.thisN"].notna()].copy()
    df["participant"] = df["participant"].astype(str)
    keep = [
        "participant", "set_size", "target_present", "condition_type",
        "corr_resp", "key_resp.keys", "key_resp.corr", "key_resp.rt",
    ]
    df = df[keep]
    df = df.rename(columns={
        "key_resp.corr": "correct",
        "key_resp.rt": "rt",
    })
    df["set_size"] = df["set_size"].astype(int)
    df["correct"] = pd.to_numeric(df["correct"], errors="coerce")
    df["rt"] = pd.to_numeric(df["rt"], errors="coerce")
    return df


def load_all() -> pd.DataFrame:
    frames = []
    for csv in sorted(DATA_DIR.glob("*_midterm_project_*.csv")):
        if csv.name.startswith("pilot_"):
            continue
        m = re.match(r"^([^_]+)_midterm_project_", csv.name)
        if not m or m.group(1) not in INCLUDED_PIDS:
            continue
        frames.append(load_participant(csv))
    if not frames:
        raise RuntimeError("No participant CSVs matched INCLUDED_PIDS")
    return pd.concat(frames, ignore_index=True)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    n0 = len(df)
    df = df.dropna(subset=["rt", "correct"])
    df = df[(df["rt"] >= RT_LOWER) & (df["rt"] <= RT_UPPER)]
    print(f"Cleaning: kept {len(df)}/{n0} trials "
          f"(removed NA + RT outside [{RT_LOWER}, {RT_UPPER}]s)")
    return df.reset_index(drop=True)


def per_subject_means(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    correct_only = df[df["correct"] == 1]
    rt_subj = (correct_only
               .groupby(["participant", "condition_type", "set_size"])["rt"]
               .mean().reset_index())
    acc_subj = (df.groupby(["participant", "condition_type", "set_size"])["correct"]
                .mean().reset_index())
    return rt_subj, acc_subj


def group_stats(subj: pd.DataFrame, value_col: str) -> pd.DataFrame:
    g = subj.groupby(["condition_type", "set_size"])[value_col]
    n = g.count()
    out = pd.DataFrame({
        "mean": g.mean(),
        "sem": g.std(ddof=1) / np.sqrt(n),
        "n": n,
    }).reset_index()
    return out


def plot_bar(stats: pd.DataFrame, value: str, ylabel: str,
             title: str, outfile: Path, ylim=None):
    set_sizes = sorted(stats["set_size"].unique())
    conds = ["feature", "conjunction"]
    x = np.arange(len(set_sizes))
    width = 0.38
    colors = {"feature": "#4C72B0", "conjunction": "#DD8452"}

    fig, ax = plt.subplots(figsize=(7, 5))
    for i, c in enumerate(conds):
        sub = stats[stats["condition_type"] == c].set_index("set_size").reindex(set_sizes)
        offset = (i - 0.5) * width
        ax.bar(x + offset, sub["mean"], width,
               yerr=sub["sem"], capsize=4,
               label=c.capitalize(), color=colors[c], edgecolor="black")
    ax.set_xticks(x)
    ax.set_xticklabels([str(s) for s in set_sizes])
    ax.set_xlabel("Set size")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    if ylim:
        ax.set_ylim(*ylim)
    ax.legend(title="Condition")
    ax.grid(axis="y", linestyle=":", alpha=0.6)
    fig.tight_layout()
    fig.savefig(outfile, dpi=150)
    print(f"Saved {outfile}")
    plt.close(fig)


def plot_search_slopes(rt_subj: pd.DataFrame, outfile: Path):
    fig, ax = plt.subplots(figsize=(7, 5))
    colors = {"feature": "#4C72B0", "conjunction": "#DD8452"}
    set_sizes = sorted(rt_subj["set_size"].unique())

    slopes = {}
    for cond in ["feature", "conjunction"]:
        sub = rt_subj[rt_subj["condition_type"] == cond]
        means = sub.groupby("set_size")["rt"].mean().reindex(set_sizes)
        sems = (sub.groupby("set_size")["rt"]
                .agg(lambda v: v.std(ddof=1) / np.sqrt(len(v)))
                .reindex(set_sizes))
        ax.errorbar(set_sizes, means.values * 1000, yerr=sems.values * 1000,
                    marker="o", capsize=4, label=cond.capitalize(),
                    color=colors[cond], linewidth=2)
        slope_ms = np.polyfit(set_sizes, means.values * 1000, 1)[0]
        slopes[cond] = slope_ms

    ax.set_xticks(set_sizes)
    ax.set_xlabel("Set size")
    ax.set_ylabel("Mean RT (ms)")
    ax.set_title("Search functions: feature vs conjunction\n"
                 f"slope feature ≈ {slopes['feature']:.1f} ms/item, "
                 f"conjunction ≈ {slopes['conjunction']:.1f} ms/item")
    ax.legend(title="Condition")
    ax.grid(linestyle=":", alpha=0.6)
    fig.tight_layout()
    fig.savefig(outfile, dpi=150)
    print(f"Saved {outfile}")
    plt.close(fig)
    return slopes


def main():
    raw = load_all()
    print(f"Loaded {raw['participant'].nunique()} participants, "
          f"{len(raw)} formal trials.")
    df = clean(raw)

    rt_subj, acc_subj = per_subject_means(df)

    rt_stats = group_stats(rt_subj, "rt")
    rt_stats["mean_ms"] = rt_stats["mean"] * 1000
    rt_stats["sem_ms"] = rt_stats["sem"] * 1000

    acc_stats = group_stats(acc_subj, "correct")
    acc_stats["mean_pct"] = acc_stats["mean"] * 100
    acc_stats["sem_pct"] = acc_stats["sem"] * 100

    print("\n=== RT (ms) by condition x set size ===")
    print(rt_stats[["condition_type", "set_size", "mean_ms", "sem_ms", "n"]]
          .to_string(index=False))
    print("\n=== Accuracy (%) by condition x set size ===")
    print(acc_stats[["condition_type", "set_size", "mean_pct", "sem_pct", "n"]]
          .to_string(index=False))

    rt_plot = rt_stats.rename(columns={"mean_ms": "mean_plot",
                                       "sem_ms": "sem_plot"})
    rt_plot["mean"] = rt_plot["mean_plot"]
    rt_plot["sem"] = rt_plot["sem_plot"]
    plot_bar(rt_plot, "rt",
             ylabel="Mean RT (ms)",
             title="Reaction time by set size and condition",
             outfile=FIG_DIR / "rt_by_setsize_condition.png")

    acc_plot = acc_stats.rename(columns={"mean_pct": "mean_plot",
                                         "sem_pct": "sem_plot"})
    acc_plot["mean"] = acc_plot["mean_plot"]
    acc_plot["sem"] = acc_plot["sem_plot"]
    plot_bar(acc_plot, "correct",
             ylabel="Accuracy (%)",
             title="Accuracy by set size and condition",
             outfile=FIG_DIR / "accuracy_by_setsize_condition.png",
             ylim=(0, 105))

    slopes = plot_search_slopes(rt_subj, FIG_DIR / "search_slopes.png")
    print(f"\nSearch slopes (ms/item): {slopes}")


if __name__ == "__main__":
    main()
