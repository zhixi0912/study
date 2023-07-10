package org.example;
public class Demo05 {
    public static void main(String[] args) {
        int i = 128;
        double b = i;
        int money = 1000000000;
        int years = 20;
        // total数值过大，内在溢出
        int total = money * years;
        long total2 = money * ((long)years);
        System.out.println(i);
        System.out.println(b);
        System.out.println(money);
        System.out.println(total);
        System.out.println(total2);
    }
}