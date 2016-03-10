import random
primenumbers = [1];
checknumbers = [1];
hold = [1];
waiting = 0;

#start
pcent = 0;



for num in range(90,999):
    if all(num%i!=0 for i in range(2,num)):
        primenumbers.append(num);
        pcent = pcent + 0.72;
        print (pcent, '% done');


for lick in range(3,101):
    if all(lick%i!=0 for i in range(2,lick)):
        checknumbers.append(lick);

primenumbers.remove(1);
checknumbers.remove(1);
print(primenumbers);
print(checknumbers);
hold.remove(1);


random.shuffle(primenumbers)



prime1 = primenumbers[1];
prime2 = primenumbers[2];
print(prime1);
print(prime2);



#get key


settings = (prime1-1) * (prime2-1);
settings2 = (prime1) * (prime2);


print(settings);
print(settings2);
x = 1;
i = 1;
t = 0;

x = 1;

i = 0;
while x == 1:
 i = i + 1;
 if i > settings:
     x = 0;
 else:
     if settings % checknumbers[i] != 0:
         print('ok');
         while x == 1:
          if settings2 % checknumbers[i] != 0:
              key = checknumbers[i];
              print('key is ', key);
              x = 0;

     else:
      print('no');
 
print(settings);
print(settings2);
x = 1;
i = 1;
t = 0;
while x == 1:
 i = i + 1;
 if ((key * i)% settings ) == 1:
     
         x = 0;
     




print(key);
print(i);


password = raw_input("enter text");

for ch in password:
    print ord(ch);
    hold.append(ord(ch));


print(hold);
testing = int(hold.pop(0))
testing = testing ** key;

print(testing);

testing = testing % settings2;

print (testing);

print (i);
#h
decr = raw_input("put in what need to be decrypted : ");


testing = int(decr) ** i;



testing = testing % settings2;

print (testing);

print chr(int(testing));


