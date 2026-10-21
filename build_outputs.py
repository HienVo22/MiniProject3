"""Write the MiniProject3 deliverables from the reviewed validation judgments.

Author values are copied from kbissonn_project_stats.csv. Validator values are
hvo5's readings of kbissonn_project_summary.csv against CodingGuide.csv.
Rows that already match are adjudicated. Rows that do not are filled with the
evidence-based proposal and left PostDiscuss = No until kbissonn confirms them.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OWNER = "kbissonn"
VALIDATOR = "hvo5"

PROJECTS = [
    "juliagaussianprocesses_abstractgps.jl",
    "pyushkevich_itksnap",
    "darrencroton_sage",
    "nanograv_enterprise",
    "nsidc_mapxmaps",
    "kinnala_scikit-fem",
    "alibaba_graphscope",
    "turinglang_bijectors.jl",
    "sandialabs_pecos",
    "sicara_tuto-fsl",
]

# Author values, in PROJECTS order, taken from kbissonn_project_stats.csv.
AUTHOR = {
    "HasRecovered": [
        "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No",
    ],
    "WhyRecovered": [
        "To fix bugs and update dependancies",
        "The main developer returned to fix bugs",
        "The main developer came back and pushed a lot of commits",
        "The new developers have taken the project and began making small bug fixes and adding new features",
        "N/A",
        "The new developer began working on the project and making changes",
        "The project started to get developed",
        "The project actually started to get developed",
        "The developer is continueing to make bug fixes and adding features",
        "N/A",
    ],
    "ActivityPattern": [
        "Declining", "Irregular", "Irregular", "Cyclical", "Irregular",
        "Declining", "Declining", "Cyclical", "Declining", "Seasonal",
    ],
    "Currentstatus": [
        "Active", "Active", "Inactive", "Active", "Inactive",
        "Active", "Active", "Active", "Active", "Inactive",
    ],
    "RecentThemes": [
        "Bug fixes:Other[code reviews]",
        "Bug fixes:Feature development",
        "Bug fixes:Documentation updates",
        "Bug fixes:Other[Unit testing]",
        "Documentation updates:Other[Announcement]",
        "Bug fixing:Other[merging branches]",
        "Bug fixes:Dependency updates",
        "Bug fixes:Feature development",
        "Bug fixes:Feature development",
        "Dependency updates:Documentation updates",
    ],
}

VALIDATOR = {
    "HasRecovered": [
        "No", "Yes", "Yes", "Yes", "No", "No", "No", "No", "Yes", "Yes",
    ],
    "WhyRecovered": [
        "N/A. The longest zero-commit run is one month (2026-02), so there is no inactivity gap to recover from.",
        "The main developer returned to fix bugs",
        "The main developer came back and pushed a lot of commits",
        "The new developers have taken the project and began making small bug fixes and adding new features",
        "N/A",
        "N/A. The longest zero-commit run is two months (2026-02 to 2026-03), under the 3-month cutoff.",
        "N/A. The longest zero-commit run is two months at startup (2020-08 to 2020-09). The project was not inactive.",
        "N/A. The longest zero-commit run is two months near the start (2019-05 to 2019-06). That is a slow start, not a recovery.",
        "Katherine Klise resumed after the 15-month gap with dependency and test-infrastructure work (pandas API renames, nose replaced by pytest), not new features.",
        "ebennequin resumed after the 4-month gap (2021-07 to 2021-10) with bug fixes and dataset utilities. The repository later stopped in June 2022.",
    ],
    "ActivityPattern": [
        "Declining", "Irregular", "Irregular", "Irregular", "Irregular",
        "Declining", "Declining", "Irregular", "Declining", "Irregular",
    ],
    "Currentstatus": [
        "Active", "Active", "Active", "Active", "Inactive",
        "Active", "Active", "Active", "Active", "Inactive",
    ],
    "RecentThemes": [
        "Bug fixes:Other[code reviews]",
        "Bug fixes:Release",
        "Feature development:Documentation updates",
        "Bug fixes:Other[Unit testing]",
        "Documentation updates:Other[Announcement]",
        "Feature development:Documentation updates",
        "Documentation updates:Automated bot contributions",
        "Automated bot contributions:Dependency updates",
        "Documentation updates:Release",
        "Bug fixes:Documentation updates",
    ],
}

EVIDENCE = {
    "HasRecovered": [
        "Longest zero-commit run is 2026-02, one month. There is no gap of 3 or more months.",
        "Longest gap is 2010-11 through 2011-03 (5 months), followed by 2,201 commits. The first commits back are bug fixes by pyushkevich.",
        "Longest gap is 2021-11 through 2024-02 (28 months), followed by 173 commits, starting with Darren Croton's Python 2 to 3 update.",
        "Longest gap is 2025-05 through 2025-07 (3 months), followed by 18 commits. Jeremy Baier adds a flat powerlaw and unit tests right after.",
        "Longest gap is 2019-10 through 2024-12 (63 months). The only later commit, on 2025-01-22, is a content edit citing a NASA direction and an executive order, not resumed development.",
        "Longest zero-commit run is 2026-02 through 2026-03 (2 months). There is no gap of 3 or more months.",
        "Longest zero-commit run is 2020-08 through 2020-09 (2 months), right after the first commit. No gap reaches 3 months, and 18,626 commits follow that hole. The author's NumCommitsAfterLastGap of 0 does not match the series.",
        "Longest zero-commit run is 2019-05 through 2019-06 (2 months), near the start. No gap reaches 3 months, and 2,204 commits follow.",
        "Longest gap is 2022-05 through 2023-07 (15 months), followed by 63 commits from Katherine Klise.",
        "Longest gap is 2021-07 through 2021-10 (4 months), followed by 68 commits. The last commit is 2022-06-02, so the repo did stop later, but that later quiet stretch is not the longest gap.",
    ],
    "WhyRecovered": [
        "Same series as HasRecovered: one empty month in 2026-02, then ordinary compat and docs commits. Nothing stopped.",
        "The commits that end the 5-month gap are bug fixes (bubble initialization, mesh saving, a typo) by pyushkevich, the main developer.",
        "Darren Croton is the first author back, with a Python 3 port, and 2025 then has 167 commits after two empty years.",
        "After the 3-month gap the new commits are a flat-powerlaw feature, unit tests, and prior-component fixes, from Jeremy Baier and other new contributors.",
        "There is no development recovery to explain. The single post-gap commit is an archival content change.",
        "Jakob Ludke does commit after the 2-month hole, but a 2-month hole is not an inactivity gap under the 3-month rule.",
        "The author treats the opening of the repository as a recovery. The commit series shows a 2-month startup hole and then continuous development.",
        "The author treats the early 2-month hole as the project finally starting. Commits before that hole already exist (toml files, Travis), and 2 months is under the cutoff.",
        "The first commits back rename pandas APIs (is_monotonic, append to concat, read_csv) and replace nose with pytest and unittest. Those are dependency and test updates.",
        "Post-gap commits fix validation accuracy, sort EasySet instances, and repair CI. ebennequin is the first author back. The project then ends in 2022, which is a later event.",
    ],
    "ActivityPattern": [
        "Yearly commits fall from 613 in 2021 to 305, 112, 98, then 174, 37. The long-run direction is down.",
        "Yearly counts swing without a direction: 237, 59, 24, 177, 24, 272, 153, 241, 185. No repeated period.",
        "Activity dies out (4 commits in 2021, none in 2022 or 2023) and then jumps to 167 in 2025. That is a break, not a smooth trend or a cycle.",
        "Yearly counts bounce (575, 149, 207, 114, 361, 73, 214, 172, 147) with no fixed interval, so this is irregular rather than cyclical.",
        "Commits arrive in bursts separated by multi-year holes (1993-1999, 2012, 2019-2024). 22 gaps last 3 months or more.",
        "Yearly commits peak at 1,111 in 2020 and 1,088 in 2021, then fall to 469, 161, 163, 77, and 30.",
        "2021 through 2024 stays high (about 3,500 to 5,000 commits a year) and then drops to 1,010 in 2025 and 62 through April 2026.",
        "Yearly counts jump around (370, 466, 230, 88, 527, 298, 251) with no repeating interval, so this is irregular rather than cyclical.",
        "Yearly commits fall from 166 and 132 in the first two years to the teens and twenties after 2018.",
        "Only two active years (116 commits, then 58) with a 4-month hole in the middle. Seasonal is not a codebook label, and there is no repeated season.",
    ],
    "Currentstatus": [
        "Last WoC commit is 2026-03-20, after the 2025-04-01 cutoff.",
        "Last WoC commit is 2025-10-27, after the cutoff.",
        "Last WoC commit is 2025-11-04, after the 2025-04-01 cutoff, so the codebook mark is Active. The author's Inactive label does not match that date.",
        "Last WoC commit is 2025-10-22, after the cutoff.",
        "Last WoC commit is 2025-01-22, before the 2025-04-01 cutoff.",
        "Last WoC commit is 2026-04-18, after the cutoff.",
        "Last WoC commit is 2026-04-21, after the cutoff.",
        "Last WoC commit is 2025-10-27, after the cutoff.",
        "Last WoC commit is 2025-04-03, two days after the cutoff, so the mark is Active.",
        "Last WoC commit is 2022-06-02, well before the cutoff.",
    ],
    "RecentThemes": [
        "Of the last 10 commits, 9 are merge commits and 1 is a small thesis fix. Bug fixes plus other (code-review merges) matches the author.",
        "The last 10 commits are DICOM hang and crash fixes, a 4.4.0 version bump, and an Ubuntu CI image bump. No feature commit. Top themes are bug fixes and a release.",
        "The last 10 commits add a dual binary/HDF5 output path, rebrand SAGE to Mimic, and clean docs. They are feature work and documentation, not bug fixes.",
        "The last 10 commits add duck-typing for Pulsar, tests for that class, and small fixes, plus merge commits. Bug fixes and other (unit tests) matches the author.",
        "The newest commit is the 2025 executive-order content change. The commits before it, years earlier, are README and documentation edits. Documentation plus other matches the author.",
        "Ignoring pure merge commits, the recent substantive commits add Example 55 and update the docs and changelog. One intersect1D fix is present but is not the top theme. Bug fixing is also not the codebook's label (the label is Bug fixes).",
        "The last 10 commits are blog posts and 'Pages update auto built' commits co-authored by github-actions. That is documentation plus an automated bot, not bug fixes or dependency bumps.",
        "The last 10 commits are repeated 'build based on' doc rebuilds, a patch bump, and an Enzyme easy_rule migration. That is automated doc builds plus dependency work, not features.",
        "The last 10 commits are release notes, a version bump, documentation edits, and a documentation requirements line. No bug-fix or feature commit.",
        "The last 10 commits fix TaskSampler and EasySet errors, fix a README notebook link, and add one warning. No dependency bump.",
    ],
}

PENDING = "Proposed from the commit series and CodingGuide.csv. kbissonn has not confirmed this row. He reviewed him2 instead, and he offered to look this log over."
MATCHED = "Independent labels match, so the author's value stands."

FIELDS = ["HasRecovered", "WhyRecovered", "ActivityPattern", "Currentstatus", "RecentThemes"]
CATEGORICAL = {"HasRecovered", "ActivityPattern", "Currentstatus"}

NOTES = {
    "HasRecovered": "Five disagreements. Gaps of 1-2 months, including GraphScope's startup hole, were coded as recoveries. tuto-fsl's longest gap did recover even though the repo later stopped. Post figures are unchanged until kbissonn confirms the proposals.",
    "WhyRecovered": "Free text, so kappa is NA. The disagreements are the same gap-definition cases, plus pecos, where the return was pandas and test-runner maintenance rather than new features.",
    "ActivityPattern": "Seasonal is not in the codebook (tuto-fsl). Cyclical was used where yearly counts bounce with no fixed period (enterprise, bijectors).",
    "Currentstatus": "One disagreement. sage's last commit is 2025-11-04, which is after the 2025-04-01 cutoff, so the codebook says Active.",
    "RecentThemes": "Kappa is NA. Most disagreements come from the latest 10 commits not showing the themes in the author's label. scikit-fem also uses 'Bug fixing' instead of 'Bug fixes'.",
}


def rows() -> list[dict]:
    out = []
    for field in FIELDS:
        for i, project in enumerate(PROJECTS):
            author = AUTHOR[field][i]
            validator = VALIDATOR[field][i]
            agree = author == validator
            out.append({
                "WOCProjectID": project,
                "ProjectOwnerNetID": OWNER,
                "ValidatorNetID": "hvo5",
                "Field": field,
                "AuthorValue": author,
                "ValidatorValue": validator,
                "PreDiscussAgreementstatus(Yes/No)": "Yes" if agree else "No",
                "KeyEvidence": EVIDENCE[field][i],
                "AdjudicatedValue": author if agree else validator,
                "ResolutionType": "AuthorKept" if agree else "ValidatorKept",
                "PostDiscussAgreementStatus": "Yes" if agree else "No",
                "Comments": MATCHED if agree else PENDING,
            })
    return out


def write_csv(path: Path, header: list[str], records: list[dict]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=header, delimiter=";", extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(records)


def cohen_kappa(left: list[str], right: list[str]) -> float:
    n = len(left)
    po = sum(a == b for a, b in zip(left, right)) / n
    cats = set(left) | set(right)
    pe = sum((left.count(c) / n) * (right.count(c) / n) for c in cats)
    if abs(1 - pe) < 1e-12:
        return 1.0 if abs(po - 1) < 1e-12 else float("nan")
    return (po - pe) / (1 - pe)


def write_tables() -> list[dict]:
    data = rows()
    log_header = [
        "WOCProjectID", "ProjectOwnerNetID", "ValidatorNetID", "Field",
        "AuthorValue", "ValidatorValue", "PreDiscussAgreementstatus(Yes/No)",
        "KeyEvidence", "AdjudicatedValue", "ResolutionType",
        "PostDiscussAgreementStatus", "Comments",
    ]
    write_csv(ROOT / "hvo5_validation_log.csv", log_header, data)

    disagreements = [r for r in data if r["PreDiscussAgreementstatus(Yes/No)"] == "No"]
    res_header = [
        "WOCProjectID", "ProjectOwnerNetID", "ValidatorNetID", "Field",
        "AuthorValue", "ValidatorValue", "AdjudicatedValue",
        "ResolutionType(AuthorKept/ValidatorKept/Compromise)",
        "PostDiscussAgreementstatus(Yes/No)", "KeyEvidence", "Comments",
    ]
    renamed = []
    for r in disagreements:
        item = dict(r)
        item["ResolutionType(AuthorKept/ValidatorKept/Compromise)"] = r["ResolutionType"]
        item["PostDiscussAgreementstatus(Yes/No)"] = r["PostDiscussAgreementStatus"]
        renamed.append(item)
    write_csv(ROOT / "hvo5_disagreement_resolution.csv", res_header, renamed)

    stats = []
    for field in FIELDS:
        subset = [r for r in data if r["Field"] == field]
        pre_yes = sum(r["PreDiscussAgreementstatus(Yes/No)"] == "Yes" for r in subset)
        post_yes = sum(r["PostDiscussAgreementStatus"] == "Yes" for r in subset)
        n_dis = sum(r["PreDiscussAgreementstatus(Yes/No)"] == "No" for r in subset)
        n_resolved = sum(
            r["PreDiscussAgreementstatus(Yes/No)"] == "No"
            and r["PostDiscussAgreementStatus"] == "Yes"
            for r in subset
        )
        if field in CATEGORICAL:
            pre_k = cohen_kappa(
                [r["AuthorValue"] for r in subset],
                [r["ValidatorValue"] for r in subset],
            )
            # No label changed after discussion, so the post kappa equals the pre kappa.
            post_k = f"{pre_k:.3f}"
            pre_k_s = f"{pre_k:.3f}"
        else:
            pre_k_s = "NA"
            post_k = "NA"
        stats.append({
            "Field": field,
            "PercentAgree_Pre": f"{pre_yes / len(subset) * 100:.1f}",
            "PercentAgree_Post": f"{post_yes / len(subset) * 100:.1f}",
            "CohenKappa_Pre": pre_k_s,
            "CohenKappa_Post": post_k,
            "NumDisagreements": n_dis,
            "NumResolved": n_resolved,
            "Notes": NOTES[field],
        })
    write_csv(
        ROOT / "hvo5_agreement_stats.csv",
        ["Field", "PercentAgree_Pre", "PercentAgree_Post", "CohenKappa_Pre",
         "CohenKappa_Post", "NumDisagreements", "NumResolved", "Notes"],
        stats,
    )
    return data


def main() -> None:
    data = write_tables()
    by_field = Counter(r["Field"] for r in data if r["PreDiscussAgreementstatus(Yes/No)"] == "No")
    print(f"rows {len(data)} disagreements {sum(by_field.values())} {dict(by_field)}")


if __name__ == "__main__":
    main()
