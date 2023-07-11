package target;

public class Demo06 {
    // 类变量 可直接使用
    static double salary = 2500;

    //属性变量 必须new后使用
    String name;
    int age;

    public static void main(String[] args) {
        int i = 10;
        System.out.println(i);
        // 变量类型 变量名 = new target.Demo06();
        Demo06 demo06 = new Demo06();
        System.out.println(demo06.age);
        System.out.println(demo06.name);

        System.out.println(salary);
    }
}
