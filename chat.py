# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 18:54:56 2023

@author: shiul
"""


def read_file(filename):
    lines = []
  #讀取檔案
    with open(filename , 'r' , encoding= 'utf-8-sig') as f:
      for line in f:
          
          if '商品,價格' in line:
              continue
          
          tmp = line.strip()
          lines.append(tmp)
    return lines

def converts(lines):
    new = []
    #person的初始值
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue    
        if person:
            new.append(person  + ': ' + line)
    return new

#實際寫入電腦檔案 字串合併時，price是數字先轉為文字
def write_file(filename, lines):
    with open(filename , 'w' , encoding= 'utf-8') as f :
        f.write('對話記錄\n')
        for line in lines:
            f.write(line + '\n')
            

def main():
    lines = read_file('input.txt')
    lines = converts(lines)
    write_file ('output.txt' , lines )


#主程式進入點    
main()