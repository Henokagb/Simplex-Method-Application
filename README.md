# Simplex-Method-Application
A use case using the mathematical method named 'Simplex' to resolve an optimisation problem



A farmer grows grains: oat, wheat, corn, barley and soy. He uses four different types of fertilizers (F1, F2, F3
et F4), in the following quantities (per ton of fertilizer in order to produce one unit of grains):

            | F1|F2 |F3 | F4 |
      ------------------------
      oat   | 1 | 1 | 2 | 0  |
      ------------------------
      wheat | 0 | 2 | 1 | 0  |
      ------------------------
      corn  | 1 | 0 | 0 | 3  |
      ------------------------
      barley| 0 | 1 | 1 | 1  |
      ------------------------
      soy   | 2 | 0 | 0 | 2  |
      ------------------------

Keeping in mind that he has limited yearly quantities of each type of fertilizer, he would like to optimize his
output according to the grains’ prices.
This program that will take his fertilizer resources and the prices of each
type of grain as parameter. It will display the quantities to produce, as well as the total value of his output.


# How to use it
## USAGE
Input:
```sh
./307multigrains -h
```
Output:
```sh
USAGE
./307multigrains n1 n2 n3 n4 po pw pc pb ps
DESCRIPTION
n1 number of tons of fertilizer F1
n2 number of tons of fertilizer F2
n3 number of tons of fertilizer F3
n4 number of tons of fertilizer F4
po price of one unit of oat
pw price of one unit of wheat
pc price of one unit of corn
pb price of one unit of barley
ps price of one unit of soy
```
## Examples:
Input1:
```sh
./307multigrains 10 100 10 0 200 200 200 200 200
```
Output1:
```sh
Resources: 10 F1, 100 F2, 10 F3, 0 F4
Oat: 0 units at $200/unit
Wheat: 10.00 units at $200/unit
Corn: 0 units at $200/unit
Barley: 0 units at $200/unit
Soy: 0 units at $200/unit
Total production value: $2000.00
```
Input2:
```sh
./307multigrains 45 41 21 63 198 259 257 231 312
```
Output2:
```
Resources: 45 F1, 41 F2, 21 F3, 63 F4
Oat: 0 units at $198/unit
Wheat: 20.00 units at $259/unit
Corn: 8.50 units at $257/unit
Barley: 1.00 units at $231/unit
Soy: 18.25 units at $312/unit
Total production value: $13289.50
```
