from complex_nums import *
def complex_nums_testing():
    t1=summ([read('999'),read('1')])
    t2=mult([read(str(j))] for j in range(10))
    t3 = summ([read(f'{str(j)}+{str(15-j)}i')] for j in range(12))
    t4 = mult([read(f'{str(j)}+{str(15-j)}i')] for j in range(1,12))
    t5 = mult([read('0')]+[read(f'{str(j)}+{str(16-j)}i')] for j in range(1,12))
    assert all([t1.c == 1000, t1.i == 0])
    assert all([t2.i==0, t2.c==0])
    assert all([t3.c == 66, t3.i == 114])
    assert t4.show == '-233654733000.00067-461196406124.99994i  517007407370.45294*e^(i10.526638831256856i)'
    assert t5.show == '0.0+0.0i  0.0*e^(17.27875959474386i)'




from QuickSort import do, ke
def QuickSort_testing():
    l1 = [0,0,0,0,0,0,0,0,0,0]
    l2 = [0]
    l3 = [4,6,3,8,5,0,8,1234,56,6598,4,6,342,374,976,4,5,7,8,1,3,0,4,245424]*999
    l4 = [1,0]
    l5 = [2,4,5,2,4,5,2,4,5,2,4,5,2,4,5,2,4,5,2,4,5]
    assert do(l1,ke) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert do(l2,ke) == [0]
    o = do(l3,ke)
    assert all(o[i] <= o[i + 1] for i in range(len(o) - 1))
    assert do(l4,ke) == [0, 1]
    assert do(l5,ke) == [2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]