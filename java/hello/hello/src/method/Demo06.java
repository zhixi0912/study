package method;

public class Demo06 {
    /**
     * 递归
     * 条件1：递归头，什么时候不调用自身。如果没有头，会陷入死循环
     * 条件2：递归体，什么时候需要调用自身方法
     * 注意：次数过大不建议使用递归
     */
    public static void main(String[] args) {
        /**
         * 求5的阶乘
         * 1! 1
         * 2! 2*1
         * 3! 3*2*1
         * 4! 4*3*2*1
         * 5! 5*4*3*2*1
         */
        Demo06 test = new Demo06();
        System.out.println(test.hashCode(5));
    }


    public int hashCode(int n) {
        if (n==1) {
            return 1;
        } else {
            return n*hashCode(n-1);
        }
    }
}
