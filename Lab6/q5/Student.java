import java.util.ArrayList;

public class Student extends Person
{
    private int rollno;
    private ArrayList<Teacher> teachers;
    public Student(String name, int age, int rollno) {
        super(name,age);
        this.rollno = rollno;
        teachers = new ArrayList<Teacher>();
    }
    public Student(Person p, int rollno){
        super(p.getName(),p.getAge());
        this.rollno = rollno;
        teachers = new ArrayList<Teacher>();
    }
    public int getRollNo() {
        return rollno;
    }
    public void addTeacher(Teacher teacher) {
        teachers.add(teacher);
    }
    public ArrayList<Teacher> getTeachers() {
        return teachers;
    }
    public void intro() {
        System.out.println("I am a Student, " + name + ", " + age +", " + rollno);  
    }
}
