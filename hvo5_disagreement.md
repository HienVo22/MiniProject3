# Disagreement Examples — hvo5 and kbissonn

Parties: hvo5 (validator) and kbissonn (author, Kaden Bissonnette).

hvo5 reviewed the 10 projects in kbissonn's MiniProject2 stats file. kbissonn's own validation log reviews him2, a student from a previous term, because hvo5's MiniProject2 repository only had Part 1 when he looked. The TA said hvo5 can substitute his own results as the agreed-upon values, so each disagreement below is resolved to the validator's evidence-based value (ValidatorKept), and PostDiscussAgreementstatus is Yes.

## Example 1 — alibaba_graphscope (HasRecovered)

**Author (kbissonn):** Yes. The notes say the project was an internal repo just getting off the ground, and NumCommitsAfterLastGap is 0.
**Validator (hvo5):** No.
**Evidence:** The longest run of zero-commit months is 2020-08 through 2020-09, two months, immediately after the 2020-07-30 open-source commit. The series has no gap of 3 or more months. 18,626 of the 18,627 commits come after that hole, so the recorded NumCommitsAfterLastGap of 0 does not match the data.
**Resolution:** ValidatorKept. A two-month startup hole is not an inactivity gap, and a recovery needs a gap to recover from.

## Example 2 — darrencroton_sage (Currentstatus)

**Author (kbissonn):** Inactive.
**Validator (hvo5):** Active.
**Evidence:** The coding guide marks a project Inactive only when its last commit is before 2025-04-01. The last commit in the WoC series is 2025-11-04 (Darren Croton's SAGE-to-Mimic rebrand and the dual binary/HDF5 output work). That is after the cutoff.
**Resolution:** ValidatorKept. This one is a date rule, not a judgment call. The 28-month gap from 2021-11 to 2024-02 is real, and both of us already agree the project recovered from it. The gap does not decide current status.

## Example 3 — sicara_tuto-fsl (HasRecovered and ActivityPattern)

**Author (kbissonn):** HasRecovered No, WhyRecovered N/A, ActivityPattern Seasonal.
**Validator (hvo5):** HasRecovered Yes, and ActivityPattern Irregular.
**Evidence:** The longest gap is 2021-07 through 2021-10, four months, and 68 commits follow it, starting with ebennequin fixing validation accuracy and EasySet. The repository does stop later: the last commit is 2022-06-02, which is why Currentstatus is Inactive for both of us. That later stop is not the longest gap. Seasonal is not one of the codebook labels (steady, rising, declining, U-shaped, stopped, cyclical, irregular), and a single 16-month span cannot show a repeated season.
**Resolution:** ValidatorKept on both fields. "The project eventually died" and "it did not recover from its longest gap" are different questions.

## Example 4 — sandialabs_pecos (WhyRecovered and RecentThemes)

**Author (kbissonn):** WhyRecovered says the developer came back to fix bugs and add features. RecentThemes is Bug fixes:Feature development.
**Validator (hvo5):** The return was dependency and test-infrastructure work. RecentThemes is Documentation updates:Release.
**Evidence:** The longest gap is 2022-05 through 2023-07, 15 months, and both of us agree the project recovered. The first commits back, from Katherine Klise, rename pandas APIs (`is_monotonic` to `is_monotonic_increasing`, `append` to `concat`) and replace nose with pytest. The latest 10 commits are release notes, a version bump, and documentation edits. None of them is a bug fix or a new feature.
**Resolution:** ValidatorKept. HasRecovered can be Yes while the reason and the latest themes are maintenance and release work.

## Example 5 — juliagaussianprocesses_abstractgps.jl (HasRecovered)

**Author (kbissonn):** Yes, to fix bugs and update dependencies. The same notes say the project does not really have gaps.
**Validator (hvo5):** No. WhyRecovered is N/A.
**Evidence:** The longest zero-commit run in a history from 2020-04 to 2026-03 is the single month 2026-02. There is no gap of 3 or more months. The commits on either side of that month are CompatHelper bumps and docs rebuilds, which is the same work the project was already doing.
**Resolution:** ValidatorKept. ActivityPattern Declining is not in dispute: yearly commits fall from 613 in 2021 to 37 in 2026. A declining project can still have no inactivity gap.
