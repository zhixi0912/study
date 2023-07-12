package method;

public class Demo1 {
    // void:返回为空
    public static void main(String[] args) {
        int sum = add(1, 2);
        System.out.println(sum);
        test();
    }
    /**
    * 修饰符 返回值类型 方法名(参数类型 参数名) {
     * ...
    * 方法体
     * ...
    * return 返回值
    * }
     */
    public static int add(int a, int b) {
        return a+b;
    }

    public static void test() {
        for (int i = 1; i<= 5; i++) {
            for (int j = 5; j>= i; j--) {
                System.out.print(" ");
            }
            for (int j = 1; j<= i; j++) {
                System.out.print("*");
            }
            for (int j = 1; j< i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
