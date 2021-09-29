import java.util.ArrayList;

public class Teacher extends Person
{
    private int salary;
    ArrayList<Student> students;
    public Teacher( String name, int age, int salary) {
        super(name,age);
        this.salary = salary;
        students = new ArrayList<Student>();
    }
    public Teacher( String name, int age) {
        super(name,age);
        this.salary = 10000;
        students = new ArrayList<Student>();
    }   
    public Teacher(Person p, int salary) {
        super(p.getName(),p.getAge());
        this.salary = salary;
    }
    public int getSalary() {
        return salary;
    }
    public void addStudent(Student stud) {
        students.add(stud);
    }
    public ArrayList<Student> getStudents() {
        return students;
    }
    public void intro() {
        System.out.println("I am a Teacher, " + name + ", " + age +", " + salary);  
    }
}
