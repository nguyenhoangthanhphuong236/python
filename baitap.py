import math 
x = 0.5; 
esp = 0.0001;
first = 1;
mu = 1;
second = first + x/1;
while ([first - second] > esp) {
    first = second
    second = first + xmu/mu;
    mu++;
}
    print (first);
