import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    static final Character REVERSE = 'R';
    static final Character DROP = 'D';
    static Boolean isError;
    static Boolean isReverse;
    static Integer T;
    static String p;
    static Integer n;
    static Deque<Integer> deque;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String args[]) throws IOException {
        input();
        bw.close();
    }
    private static void input() throws IOException {
        T = Integer.parseInt(br.readLine());
        for(int i=0;i<T;i++){
            isError = Boolean.FALSE;
            isReverse = Boolean.FALSE;
            p = br.readLine();
            n = Integer.parseInt(br.readLine());
            if(n==0){
                br.readLine();
                if(p.contains("D")){
                    isError = Boolean.TRUE;
                    bw.write("error");
                    bw.newLine();
                }
                else{
                    bw.write("[]");
                    bw.newLine();
                }
            }
            else {
                makeArr(br.readLine());
                logic();
                output();
            }

        }
    }
    private static void output() throws IOException {
        if(isError) {
            bw.write("error");
            bw.newLine();
            return;
        }
        bw.write("[");
        int i = 1;
        if(!isReverse) writCorrect();
        else reverseWrite();
        bw.write("]");
        bw.newLine();
    }
    private static void writCorrect() throws IOException {
        int size = deque.size();
        for(int i=0;i<size;i++){
            bw.write(deque.pollFirst() + (i==size-1?"":","));
        }
    }
    private static void reverseWrite() throws IOException{
        int size = deque.size();
        for(int i=0;i<size-1;i++){
            bw.write(deque.pollLast() +",");
        }
        bw.write(deque.poll()+"");
    }
    private static void logic(){
        for(int i=0;i<p.length();i++){
            Character order = p.charAt(i);
            if(order.equals(DROP)){
                if(deque.isEmpty()){
                    isError = Boolean.TRUE;
                    return;
                }
                if(isReverse) deque.pollLast();
                else deque.pollFirst();
            }
            if(order.equals(REVERSE)){
                isReverse = !isReverse;
            }
        }
    }
    private static void makeArr(String input){
        deque= new ArrayDeque<>();
        input =input.replace("[","");
        input = input.replace("]","");
        for(String num: input.split(",")){
            deque.add(Integer.parseInt(num));
        }
    }
}