# -*- coding: utf-8 -*-
"""Category3_prob2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ic_QPW4e1q3dEOE7bo6o7G3CKgnnXsue
"""

T = int(input())
count = 0

if T < 1 or T > 1000:
  print("invalid input")
while count < T:
  if T < 1 or T > 1000:
    break
  count = count + 1
  a,b = map(int,input().split())
  if a < 100 or a > 200:
    print("invalid input")
    break
  elif b < 100 or b > 200:
    print("invalid input")
    break
    
  def height(x,y):
    if x>y:
      return "A"
    elif y>x:
      return "B"
  print(height(a,b))