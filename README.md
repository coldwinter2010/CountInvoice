CountInvoice
============

based on the number of invoices and their denominations, get a sub-set of invoices that have a maximum sum less than the target number.
大家在现实生活中，往往会遇到凑发票的情景，具体情况如下：
报销额度X元，你手头有发票N张，面值分别是a1..aN，如何凑出最接近（不大于）X元的总额？
抽象成数学问题就是：已知一堆数的集合与一个目标值，如何找到一个子集，使得子集内数的和最接近但不大于目标值。
方法是动态规划。语言是Python。欢迎试用~
