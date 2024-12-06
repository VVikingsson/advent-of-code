package day06;

public class State {
    public String dir;
    public int[] tuple;
    public State(String dir, int i, int j) {
        this.dir = dir;
        this.tuple = new int[]{i, j};
    }
}
