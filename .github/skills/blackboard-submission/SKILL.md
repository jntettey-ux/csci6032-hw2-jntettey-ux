---
name: blackboard-submission
description: Submission skill for CSCI 6032 Homework 2 that validates repo state, packages clean archive, and stages Blackboard submission with human confirmation.
---

1. Confirm that it is operating in the expected homework repository.
2. Run a preflight that checks the current branch, git status, recent commits, expected remote URL, and required files.
3. Stop if the tree is not clean, required artifacts are absent, or unresolved secrets/private data are apparent.
4. Confirm that the reviewed branch has been pushed.
5. Prepare csci6032-hw2-jntettey-ux.tar.gz from the committed HEAD without including .git, credentials, caches, or unrelated files.
6. List the archive contents and show the exact notebook, archive, repository URL, and submission text it proposes to use.
7. Support a dry run that performs every possible check without opening Blackboard or submitting.
8. Ask before opening or controlling the Blackboard tab.
9. Require the student to authenticate personally; never request, read, store, type, or expose credentials.
10. Navigate only to this homework's submission page and stage the required files and repository URL.
11. Stop immediately before the final, irreversible submission action and show the student exactly what will be submitted.
12. Require explicit confirmation at that point. A prior general approval is not sufficient.
13. After confirmation, complete the submission, verify the confirmation page or receipt, and report the result.
14. Do not commit Blackboard screenshots, receipts, browser data, or personal information to the public repository.