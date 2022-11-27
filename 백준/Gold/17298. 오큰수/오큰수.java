import java.io.*;
import java.util.Stack;

public class Main {
    static Integer[] array;
    static Integer n;
    static Stack<Integer[]> stack;
    static Integer[] result;
    public static void main(String args[]) throws IOException {
        input();
        mainLogic();
        output();
    }
    private static void mainLogic(){
        stack = new Stack<>();
        result = new Integer[n];
        for(int i=0;i<n;i++){
            result[i] = -1;
        }
        for(int i=0;i<n;i++){
            if(!stack.empty()){
                while(stack.peek()[0]<array[i]){
                    result[stack.pop()[1]]= array[i];
                    if(stack.empty()) break;
                }
            }
            stack.add(new Integer[]{array[i],i});
        }
    }
    private static void testInput(){
        n = 4;
        array = new Integer[]{3,5,2,7};
    }
    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        array= new Integer[n];
        int i =0;
        for(String num: br.readLine().split(" ")){
            array[i] = Integer.parseInt(num);
            i++;
        }
        br.close();
    }
    private static void output() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int i=0;i<n;i++){
            bw.write((i==0? "": " ") + result[i]);
        }
        bw.close();
    }
}