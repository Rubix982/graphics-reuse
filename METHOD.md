# Method

How an entry gets made and tested. Adapted from the method of `style`, a sibling library, which learned several of these steps from its own results (its cards C-003 and C-007). Where a step comes from there, it says so.

## 1. Pick the repeated work, then sources

Start from a kind of repeated work ("a garment already draped on one body is draped again on another"), not from a paper you admire. Then find where some field has dealt with it: papers, course notes, the documentation of solvers that do it in production.

Get the **primary** source: the paper, the official slides, the manual page, not a blog post about it. Put every source in the entry's `source_docs`. If a source was only seen second-hand (a mirror of slides, a summary), say so.

Look at several sources **that cover different cases**: different fields, different kinds of input. `style`'s C-003 found that three manuals for one bookcase agreed on facts that half-failed on a chair, a chest of drawers and a lamp. Sort what the sources say about when the reuse works into:

- **constant**: holds whatever the case, usually because it follows from how the method works;
- **conditional**: holds only when the work has a particular property. Name the property. Expect most conditions to be this kind;
- **varies**: sources disagree without a clear reason. Record the disagreement.

## 2. Read for the numbers and the limits

Go source by source. Write down what is reported before deciding what it means.

- The speedup, on what input, against what baseline, on what hardware.
- What the reuse costs: memory, precomputation, implementation inside a solver you may not control.
- Where the source's own method fails or isn't used. Papers state limits in their last sections and in the cases they leave out; both go into section 5 of the entry.

## 2b. Check what an agent already does

From `style`'s METHOD.md step 2b. Before writing the entry, give one fresh agent a description of the repeated work with **no entry and no hint of the technique**, and ask how it would avoid redoing the work and when that would be safe. Record in `agent_baseline` which techniques it proposed and which of the entry's conditions it named.

An entry should carry what the agent doesn't already know. `style`'s C-007 found the agent already followed 5 of an entry's 6 rules, and the entry's extra material made the result worse. Expect this more often here than in design, because models have read the graphics literature. An entry whose technique and conditions the agent names unprompted can still be worth keeping as part of the map, but it adds nothing as agent context, and its header should say so.

The baseline goes stale when the model changes. Re-check it before relying on an old one.

Step 2b is circular when the entry was written by the same model from its own knowledge: the agent will name what the entry says because the entry came from the same place. R-011 found this on the three seed entries, which were written from abstracts and memory. What the step can show is the part of an entry that came from outside the model: a measurement, or a detail read in a source in full. Read the sources in full before writing (step 2), and expect the entry's value to sit in those parts.

## 3. Write the entry

Copy `entries/_template.md` to `entries/<technique>.md`. Before calling it done:

- Every number says where it came from: which source and which table, or which measurement.
- Every condition in section 4 is marked (paper), (measured) or (reasoned).
- `reuse_changes` is filled. When the reuse changes the answer, section 4 is where the entry earns its place. When it changes only the cost, section 5 should say how the slowdown shows and when to stop reusing (a refit tree is rebuilt once it gets too loose).
- The one-sentence statement at the top could be observed to be false. A number beats an adjective.
- One mechanism per entry. If a paper combines two, write two entries and name the other in `also_teaches`.

## 4. Test it by measurement

An entry isn't trusted until a reuse built from it has been measured against the full computation. That needs a test bed: a real pipeline where the repeated work happens and where the answer can be checked. The first is a private Blender garment pipeline. Tests run in the test bed's own repository by its own rules; this repository records the result.

1. **Open a card first**, with both branches written before anything runs.
2. **Fix the arms.** The full arm does the computation from scratch. The reuse arm does it with the technique. Same inputs, same settings, same seeds.
3. **Run several seeds of the full arm.** How much they differ from each other is the yardstick for "the same answer".
4. **Measure** each arm's time, and the test bed's checks (for cloth: cloth crossing cloth, landmark lengths, silhouette).
5. **Decide.** The reuse is valid for that test bed if its checks fall within the full arm's seed-to-seed spread. Record the time saved beside it.
6. **Write the result in the card**, including anything the run showed was wrong with the card's measures. Update the entry's `tested_in`.

### 4b. Test it as agent context (later)

For the agent purpose (`threads.md`, T-002): give a fresh agent the repeated work with and without the entry, and count how many of its proposals pass step 4's check. Not before one test bed has enough tested entries to run it on.

## Known weaknesses of this method

- One test bed at a time. A reuse that holds in the test bed's cloth may not hold in another solver. `tested_in` names where it was measured, and nothing more is claimed.
- Timings are noisy. A 2026 replay of software-optimisation benchmarks found only 39 of GSO's 102 tasks gave stable results across hardware (arXiv 2607.01211). Time each arm more than once on one machine and report the spread.
- The seed-to-seed spread is only as good as the number of seeds behind it.
- Step 2b uses one agent run, and agents vary between runs. It is also scored by a model of the same family as the agent.
- Entries from reading alone carry the sources' own conditions, which are stated for the paper's test scenes, not for yours.
