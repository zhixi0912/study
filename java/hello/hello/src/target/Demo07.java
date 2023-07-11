package target;

public class Demo07 {
    public static void main(String[] args) {
        //幂运算 2的3次方
        double pow = Math.pow(2, 3);
        System.out.println(pow);

        // 逻辑运算
        boolean a = true;
        boolean b = false;
        System.out.println("a && b:" + (a && b));
        System.out.println("a || b:" + (a || b));
        System.out.println("!(a && b):" + !(a && b));

        // 短路运算
        int c = 5;
        boolean d = (c<4)&&(c++<4);
        System.out.println(d);
        System.out.println(c);

    }

}
