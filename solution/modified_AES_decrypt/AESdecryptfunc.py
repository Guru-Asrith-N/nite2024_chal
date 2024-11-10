from BitVector import * #use BitVector class created by Avinash Kak (kak@purdue.edu) at https://engineering.purdue.edu/kak/dist/BitVector-3.4.4.html
import math #import math module to use function such as ceiling

#findroundkey takes in the hex pass string of the size 32 and an integer value between 1-10 for the round number. After operations are performed, a hex pass string of the size 32 is generated
def findroundkey(temp1, case):
    w0=temp1[0:8]
    w1=temp1[8:16]
    w2=temp1[16:24]
    w3=temp1[24:32]
    temp2=temp1[24:32]
    temp2=shiftrow(temp2)
    temp2=subbyte(temp2)
    if(case==1):
        temp2=xor(temp2,'01000000')
    elif(case==2):
        temp2 = xor(temp2, '02000000')
    elif (case == 3):
        temp2 = xor(temp2, '04000000')
    elif (case == 4):
        temp2 = xor(temp2, '08000000')
    elif (case == 5):
        temp2 = xor(temp2, '10000000')
    elif (case == 6):
        temp2 = xor(temp2, '20000000')
    elif (case == 7):
        temp2 = xor(temp2, '40000000')
    elif (case == 8):
        temp2 = xor(temp2, '80000000')
    elif (case == 9):
        temp2 = xor(temp2, '1b000000')
    elif (case == 10):
        temp2 = xor(temp2, '36000000')
    w4=xor(w0, temp2)
    w5=xor(w1, w4)
    w6=xor(w2, w5)
    w7=xor(w3, w6)
    temp3=w4+w5+w6+w7
    return temp3

#xor takes in two hex strings of the same size, then peforms an xor on these operands to produce a singular hex string
def xor(temp1,temp2):
        temp1=BitVector(hexstring=temp1)
        temp2=BitVector(hexstring=temp2)
        temp3=temp1^temp2
        return temp3.get_bitvector_in_hex()

#subbyte function takes in a hex string to puts it through the lookup table to ouput a converted hex string
def subbyte(myhexstring):
    loop2 = 0
    temp=""
    temp2=""
    part0 = ['63', '9b', '4b', '7b', 'ea', '73', '53', '06', 'a9', '25', '43', '71', 'da', '4e', '70', 'cb']
    part1 = ['f6', 'e4', '36', '1b', 'fa', '3f', '47', 'aa', '10', '8e', 'e0', '50', '9c', '80', 'eb', 'a6']
    part2 = ['48', '1a', '6c', 'c1', 'c9', '59', '4a', '96', '89', '00', '02', '2a', '2b', 'be', '29', '0d']
    part3 = ['85', '46', '61', '66', 'bd', 'cc', '05', 'fc', '45', 'ed', 'a4', 'e2', '72', '41', 'e8', '0b']
    part4 = ['35', '64', '91', 'fd', '7d', 'd3', 'ff', 'a0', 'ef', '79', 'ce', '68', '31', '62', '51', '84']
    part5 = ['6f', '2e', 'a5', '12', 'a1', '9a', '28', '7f', 'f3', '76', 'd8', '39', 'f7', '97', 'bf', '56']
    part6 = ['ae', '52', 'f0', '7a', '67', '17', '69', '04', '07', '3a', 'e5', '5b', 'af', '99', '5c', 'b0']
    part7 = ['2f', '60', 'a7', '54', 'ec', '1c', 'b9', '0a', '98', 'c8', 'fe', '21', 'ad', '5a', '6a', 'ee']
    part8 = ['16', '95', '6d', '92', '5f', '4c', '87', '4d', '86', '40', 'db', '19', '83', '1f', '3d', '6b']
    part9 = ['a3', '24', '57', '9e', 'e1', 'f1', 'ac', 'b4', 'c7', 'd2', 'b8', '8d', 'de', 'df', '75', '7e']
    part10 = ['a2', 'e9', 'f9', 'f5', '37', 'c5', '81', '9f', 'e6', '6e', '90', 'e3', '2c', '0c', '82', '3b']
    part11 = ['42', 'b6', '49', '13', '14', '0e', 'd7', '30', '93', 'cf', '8a', 'f2', '03', 'fb', 'd0', 'b5']
    part12 = ['f8', 'bb', '01', 'd1', '9d', 'c0', '88', 'c6', 'b2', '1e', '8b', '5d', '77', '18', '74', 'f4']
    part13 = ['ab', 'd9', '08', 'c3', 'b7', '65', 'ca', 'd5', '23', '09', '4f', '38', 'c4', '26', '1d', 'dc']
    part14 = ['22', 'ba', 'bc', '2d', '33', '3e', 'd4', '8c', '7c', 'dd', '44', '32', 'd6', '0f', 'b1', '5e']
    part15 = ['94', '20', '34', '15', '58', 'c2', 'e7', 'b3', '27', '3c', '11', '55', 'a8', '8f', '78', 'cd']


    lookuptable=[part0,part1,part2,part3,part4,part5,part6,part7,part8,part9,part10,part11,part12,part13,part14,part15]

    #print("The string size is ", len(myhexstring), " and the loop will run", math.ceil(len(myhexstring)/2), " times." )
    for loop in range(0, math.ceil(len(myhexstring)/2) ):
        x = ""
        y = ""
        x=myhexstring[loop2]
        y=myhexstring[loop2+1]
        #convert character to integer
        if(x=='0'):
            x=0
        elif (x=='1'):
            x=1
        elif (x=='2'):
            x=2
        elif (x=='3'):
            x=3
        elif (x=='4'):
            x=4
        elif (x=='5'):
            x=5
        elif (x=='6'):
            x=6
        elif (x=='7'):
            x=7
        elif (x =='8'):
            x=8
        elif (x=='9'):
            x=9
        elif(x=='a'):
            x=10
        elif(x=='b'):
            x=11
        elif (x=='c'):
            x=12
        elif (x=='d'):
            x=13
        elif (x=='e'):
            x=14
        elif (x=='f'):
            x=15

        if(y=='0'):
            y=0
        elif (y=='1'):
            y=1
        elif (y=='2'):
            y=2
        elif (y=='3'):
            y=3
        elif (y=='4'):
            y=4
        elif (y=='5'):
            y=5
        elif (y=='6'):
            y=6
        elif (y=='7'):
            y=7
        elif (y =='8'):
            y=8
        elif (y=='9'):
            y=9
        elif(y=='a'):
            y=10
        elif(y=='b'):
            y=11
        elif (y=='c'):
            y=12
        elif (y=='d'):
            y=13
        elif (y=="e"):
            y=14
        elif (y=="f"):
            y=15
        temp=lookuptable[x][y]
        loop2=loop2+2
        temp2 = temp2 + temp
    return temp2

#shiftrow takes in a hex string of the size 8 or 32, then performs a shifting operation to output the a converted hex string
def shiftrow(temp2):

    if(len(temp2)==8):
        temp3=temp2[2]+temp2[3]+temp2[4]+temp2[5]+temp2[6]+temp2[7]+temp2[0]+temp2[1]
        return temp3
    else:
        temp3=temp2[0]+temp2[1]+temp2[10]+temp2[11]+temp2[20]+temp2[21]+temp2[30]+temp2[31]+temp2[8]+temp2[9]+temp2[18]+temp2[19]+\
              temp2[28] + temp2[29] + temp2[6] + temp2[7] + temp2[16] + temp2[17] + temp2[26] + temp2[27] + temp2[4] + temp2[5] + \
              temp2[14] + temp2[15] + temp2[24] + temp2[25] + temp2[2] + temp2[3] + temp2[12] + temp2[13] + temp2[22] + temp2[23]
        return temp3

# shiftrow takes in a hex string of the size 8 or 32, then performs a shifting operation to output the a converted hex string
def invshiftrow(temp2):

    if (len(temp2) == 8):
        temp3 = temp2[6] + temp2[7] + temp2[0] + temp2[1] + temp2[2] + temp2[3] + temp2[4] + temp2[5]#in progress
        return temp3
    else:#replace
        #temp3=temp2[0]+temp2[1]+temp2[10]+temp2[11]+temp2[20]+temp2[21]+temp2[30]+temp2[31]+temp2[8]+temp2[9]\
        #      +temp2[18]+temp2[19]+temp2[28] + temp2[29] + temp2[6] + temp2[7] + temp2[16] + temp2[17] + temp2[26] + temp2[27]\
        #      + temp2[4] + temp2[5] + temp2[14] + temp2[15] + temp2[24] + temp2[25] + temp2[2] + temp2[3] + temp2[12] + temp2[13]\
        #      + temp2[22] + temp2[23]
        # 00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31
        # 00,01,10,11,20,21,30,31,08,09,18,19,28,29,06,07,16,17,26,27,04,05,14,15,24,25,02,03,12,13,22,23
        # working on this, second line
        temp3=temp2[0]+temp2[1]+temp2[26]+temp2[27]+temp2[20]+temp2[21]+temp2[14]+temp2[15]+temp2[8]+temp2[9]\
              +temp2[2]+temp2[3]+temp2[28] + temp2[29] + temp2[22] + temp2[23] + temp2[16] + temp2[17] + temp2[10] + temp2[11]\
              + temp2[4] + temp2[5] + temp2[30] + temp2[31] + temp2[24] + temp2[25] + temp2[18] + temp2[19] + temp2[12] + temp2[13]\
              + temp2[6] + temp2[7]

        return temp3


#subbyte function takes in a hex string to puts it through the lookup table to ouput a converted hex string
def invsubbyte(myhexstring):
    loop2 = 0
    temp=""
    temp2=""
    part0 = ['29', 'c2', '2a', 'bc', '67', '36', '07', '68', 'd2', 'd9', '77', '3f', 'ad', '2f', 'b5', 'ed']#inverse sbox 
    part1 = ['18', 'fa', '53', 'b3', 'b4', 'f3', '80', '65', 'cd', '8b', '21', '13', '75', 'de', 'c9', '8d']#inverse sbox 
    part2 = ['f1', '7b', 'e0', 'd8', '91', '09', 'dd', 'f8', '56', '2e', '2b', '2c', 'ac', 'e3', '51', '70']#inverse sbox 
    part3 = ['b7', '4c', 'eb', 'e4', 'f2', '40', '12', 'a4', 'db', '5b', '69', 'af', 'f9', '8e', 'e5', '15']#inverse sbox 
    part4 = ['89', '3d', 'b0', '0a', 'ea', '38', '31', '16', '20', 'b2', '26', '02', '85', '87', '0d', 'da']#inverse sbox 
    part5 = ['1b', '4e', '61', '06', '73', 'fb', '5f', '92', 'f4', '25', '7d', '6b', '6e', 'cb', 'ef', '84']#inverse sbox 
    part6 = ['71', '32', '4d', '00', '41', 'd5', '33', '64', '4b', '66', '7e', '8f', '22', '82', 'a9', '50']#inverse sbox 
    part7 = ['0e', '0b', '3c', '05', 'ce', '9e', '59', 'cc', 'fe', '49', '63', '03', 'e8', '44', '9f', '57']#inverse sbox 
    part8 = ['1d', 'a6', 'ae', '8c', '4f', '30', '88', '86', 'c6', '28', 'ba', 'ca', 'e7', '9b', '19', 'fd']#inverse sbox
    part9 = ['aa', '42', '83', 'b8', 'f0', '81', '27', '5d', '78', '6d', '55', '01', '1c', 'c4', '93', 'a7']#inverse sbox
    part10 = ['47', '54', 'a0', '90', '3a', '52', '1f', '72', 'fc', '08', '17', 'd0', '96', '7c', '60', '6c']#inverse sbox
    part11 = ['6f', 'ee', 'c8', 'f7', '97', 'bf', 'b1', 'd4', '9a', '76', 'e1', 'c1', 'e2', '34', '2d', '5e']#inverse sbox
    part12 = ['c5', '23', 'f5', 'd3', 'dc', 'a5', 'c7', '98', '79', '24', 'd6', '0f', '35', 'ff', '4a', 'b9']#inverse sbox
    part13 = ['be', 'c3', '99', '45', 'e6', 'd7', 'ec', 'b6', '5a', 'd1', '0c', '8a', 'df', 'e9', '9c', '9d']#inverse sbox
    part14 = ['1a', '94', '3b', 'ab', '11', '6a', 'a8', 'f6', '3e', 'a1', '04', '1e', '74', '39', '7f', '48']#inverse sbox
    part15 = ['62', '95', 'bb', '58', 'cf', 'a3', '10', '5c', 'c0', 'a2', '14', 'bd', '37', '43', '7a', '46']#inverse sbox


    lookuptable=[part0,part1,part2,part3,part4,part5,part6,part7,part8,part9,part10,part11,part12,part13,part14,part15]

    #print("The string size is ", len(myhexstring), " and the loop will run", math.ceil(len(myhexstring)/2), " times." )
    for loop in range(0, math.ceil(len(myhexstring)/2) ):
        x = ""
        y = ""
        x=myhexstring[loop2]
        y=myhexstring[loop2+1]
        #convert character to integer
        if(x=='0'):
            x=0
        elif (x=='1'):
            x=1
        elif (x=='2'):
            x=2
        elif (x=='3'):
            x=3
        elif (x=='4'):
            x=4
        elif (x=='5'):
            x=5
        elif (x=='6'):
            x=6
        elif (x=='7'):
            x=7
        elif (x =='8'):
            x=8
        elif (x=='9'):
            x=9
        elif(x=='a'):
            x=10
        elif(x=='b'):
            x=11
        elif (x=='c'):
            x=12
        elif (x=='d'):
            x=13
        elif (x=='e'):
            x=14
        elif (x=='f'):
            x=15

        if(y=='0'):
            y=0
        elif (y=='1'):
            y=1
        elif (y=='2'):
            y=2
        elif (y=='3'):
            y=3
        elif (y=='4'):
            y=4
        elif (y=='5'):
            y=5
        elif (y=='6'):
            y=6
        elif (y=='7'):
            y=7
        elif (y =='8'):
            y=8
        elif (y=='9'):
            y=9
        elif(y=='a'):
            y=10
        elif(y=='b'):
            y=11
        elif (y=='c'):
            y=12
        elif (y=='d'):
            y=13
        elif (y=="e"):
            y=14
        elif (y=="f"):
            y=15
        temp=lookuptable[x][y]
        loop2=loop2+2
        temp2 = temp2 + temp
    return temp2

#mix column takes in an a 128 bit string, performs a series of matrix multiplication to output a hex string
def invmixcolumn(bv3):
        bv01 = (bv3[0:8])
        bv23 = (bv3[8:16])
        bv45 = (bv3[16:24])
        bv67 = (bv3[24:32])
        bv89 = (bv3[32:40])
        bv1011 = (bv3[40:48])
        bv1213 = (bv3[48:56])
        bv1415 = (bv3[56:64])
        bv1617 = (bv3[64:72])
        bv1819 = (bv3[72:80])
        bv2021 = (bv3[80:88])
        bv2223 = (bv3[88:96])
        bv2425 = (bv3[96:104])
        bv2627 = (bv3[104:112])
        bv2829 = (bv3[112:120])
        bv3031 = (bv3[120:128])

        eightlim = BitVector(bitstring='100011011')
        one = BitVector(bitstring='0001')
        two = BitVector(bitstring='0010')
        three = BitVector(bitstring='0011')
        nine = BitVector(bitstring='1001')
        eleven = BitVector(bitstring='1011')
        thirteen = BitVector(bitstring='1101')
        fourteen = BitVector(bitstring='1110')

        tempbv1 = bv01.gf_multiply_modular(fourteen, eightlim, 8) #done
        tempbv2 = bv23.gf_multiply_modular(eleven, eightlim, 8)
        tempbv3 = bv45.gf_multiply_modular(thirteen, eightlim, 8)
        tempbv4 = bv67.gf_multiply_modular(nine, eightlim, 8)
        newbv01 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv01.gf_multiply_modular(nine, eightlim, 8) #done
        tempbv2 = bv23.gf_multiply_modular(fourteen, eightlim, 8)
        tempbv3 = bv45.gf_multiply_modular(eleven, eightlim, 8)
        tempbv4 = bv67.gf_multiply_modular(thirteen, eightlim, 8)
        newbv23 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv01.gf_multiply_modular(thirteen, eightlim, 8)#done
        tempbv2 = bv23.gf_multiply_modular(nine, eightlim, 8)
        tempbv3 = bv45.gf_multiply_modular(fourteen, eightlim, 8)
        tempbv4 = bv67.gf_multiply_modular(eleven, eightlim, 8)
        newbv45 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv01.gf_multiply_modular(eleven, eightlim, 8)#done
        tempbv2 = bv23.gf_multiply_modular(thirteen, eightlim, 8)
        tempbv3 = bv45.gf_multiply_modular(nine, eightlim, 8)
        tempbv4 = bv67.gf_multiply_modular(fourteen, eightlim, 8)
        newbv67 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4




        tempbv1 = bv89.gf_multiply_modular(fourteen, eightlim, 8) #done
        tempbv2 = bv1011.gf_multiply_modular(eleven, eightlim, 8)
        tempbv3 = bv1213.gf_multiply_modular(thirteen, eightlim, 8)
        tempbv4 = bv1415.gf_multiply_modular(nine, eightlim, 8)
        newbv89 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv89.gf_multiply_modular(nine, eightlim, 8) #done
        tempbv2 = bv1011.gf_multiply_modular(fourteen, eightlim, 8)
        tempbv3 = bv1213.gf_multiply_modular(eleven, eightlim, 8)
        tempbv4 = bv1415.gf_multiply_modular(thirteen, eightlim, 8)
        newbv1011 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv89.gf_multiply_modular(thirteen, eightlim, 8)#done
        tempbv2 = bv1011.gf_multiply_modular(nine, eightlim, 8)
        tempbv3 = bv1213.gf_multiply_modular(fourteen, eightlim, 8)
        tempbv4 = bv1415.gf_multiply_modular(eleven, eightlim, 8)
        newbv1213 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv89.gf_multiply_modular(eleven, eightlim, 8)#done
        tempbv2 = bv1011.gf_multiply_modular(thirteen, eightlim, 8)
        tempbv3 = bv1213.gf_multiply_modular(nine, eightlim, 8)
        tempbv4 = bv1415.gf_multiply_modular(fourteen, eightlim, 8)
        newbv1415 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4




        tempbv1 = bv1617.gf_multiply_modular(fourteen, eightlim, 8) #done
        tempbv2 = bv1819.gf_multiply_modular(eleven, eightlim, 8)
        tempbv3 = bv2021.gf_multiply_modular(thirteen, eightlim, 8)
        tempbv4 = bv2223.gf_multiply_modular(nine, eightlim, 8)
        newbv1617 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv1617.gf_multiply_modular(nine, eightlim, 8) #done
        tempbv2 = bv1819.gf_multiply_modular(fourteen, eightlim, 8)
        tempbv3 = bv2021.gf_multiply_modular(eleven, eightlim, 8)
        tempbv4 = bv2223.gf_multiply_modular(thirteen, eightlim, 8)
        newbv1819 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv1617.gf_multiply_modular(thirteen, eightlim, 8)#done
        tempbv2 = bv1819.gf_multiply_modular(nine, eightlim, 8)
        tempbv3 = bv2021.gf_multiply_modular(fourteen, eightlim, 8)
        tempbv4 = bv2223.gf_multiply_modular(eleven, eightlim, 8)
        newbv2021 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv1617.gf_multiply_modular(eleven, eightlim, 8)#done
        tempbv2 = bv1819.gf_multiply_modular(thirteen, eightlim, 8)
        tempbv3 = bv2021.gf_multiply_modular(nine, eightlim, 8)
        tempbv4 = bv2223.gf_multiply_modular(fourteen, eightlim, 8)
        newbv2223 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4





        tempbv1 = bv2425.gf_multiply_modular(fourteen, eightlim, 8) #done
        tempbv2 = bv2627.gf_multiply_modular(eleven, eightlim, 8)
        tempbv3 = bv2829.gf_multiply_modular(thirteen, eightlim, 8)
        tempbv4 = bv3031.gf_multiply_modular(nine, eightlim, 8)
        newbv2425 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv2425.gf_multiply_modular(nine, eightlim, 8) #done
        tempbv2 = bv2627.gf_multiply_modular(fourteen, eightlim, 8)
        tempbv3 = bv2829.gf_multiply_modular(eleven, eightlim, 8)
        tempbv4 = bv3031.gf_multiply_modular(thirteen, eightlim, 8)
        newbv2627 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv2425.gf_multiply_modular(thirteen, eightlim, 8)#done
        tempbv2 = bv2627.gf_multiply_modular(nine, eightlim, 8)
        tempbv3 = bv2829.gf_multiply_modular(fourteen, eightlim, 8)
        tempbv4 = bv3031.gf_multiply_modular(eleven, eightlim, 8)
        newbv2829 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        tempbv1 = bv2425.gf_multiply_modular(eleven, eightlim, 8)#done
        tempbv2 = bv2627.gf_multiply_modular(thirteen, eightlim, 8)
        tempbv3 = bv2829.gf_multiply_modular(nine, eightlim, 8)
        tempbv4 = bv3031.gf_multiply_modular(fourteen, eightlim, 8)
        newbv3031 = tempbv1 ^ tempbv2 ^ tempbv3 ^ tempbv4

        newbv = newbv01 + newbv23 + newbv45 + newbv67 + newbv89 + newbv1011 + newbv1213 + newbv1415 + newbv1617 + newbv1819 + newbv2021 + newbv2223 + newbv2425 + newbv2627 + newbv2829 + newbv3031
        newbvashex = newbv.get_bitvector_in_hex()
        return newbvashex