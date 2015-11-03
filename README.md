# LintCode ![Language](https://img.shields.io/badge/language-Python-blue.svg) ![License](https://img.shields.io/badge/license-Apache-red.svg)
Python in Action.  

## Contents
Only unique questions from [LintCode](https://github.com/algorhythms/LintCode) are included. Duplicated questions of [LeetCode](https://github.com/idf/LeetCode) are excluded, which can be found in [ https://github.com/idf/LeetCode](https://github.com/idf/LeetCode) instead.
### Python
This repo mainly uses Python. To run in Python:
```bash
python <QuestionName>.py
```
If you encountered `Class Already Defined` compilation problem in OJ, please remove `TreeNode`, `GraphNode` or etc. 
### Java
Some algorithms in Python cannot pass the OJ due to OJ bugs; thus the alternative solutions in java in the exactly same algorithm are provided. To run in Java:
```bash
cd LintCode/java/src/main/java
javac <PackageName>/Solution.java
java -ea <PackageName>/Solution  # -ea: enable assertion
```
### Notes: TLE & MLE
Failed attempts are kept in the source code as documentation, which are annotated as TLE (Time Limit Exceeds) or MLE (Memory Limit Exceeds).

## Online Judges 
* [LintCode OJ](http://lintcode.com/en/daily/)
* [LeetCode OJ](https://oj.leetcode.com/problems/)

## LintCode Copyright
Most of the code are from the section tag of [LintCode Copyright](http://lintcode.com/tag/lintcode-copyright)
