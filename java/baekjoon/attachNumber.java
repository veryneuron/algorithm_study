package baekjoon;
import java.util.*;
import java.io.*;

// 2667

public class attachNumber {
    static String[][] map;
    static Boolean[][] visited;
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new String[N][N];
        visited = new Boolean[N][N];
        for(int i=0; i<N; i++) {
            String[] ch = br.readLine().split("");
            for(int j=0; j<N; j++) {
                map[i][j] = ch[j];
                visited[i][j] = false;
            }
        }
        List<Integer> result = new ArrayList<>();
        for (int row=0; row < N; row++) {
            for (int col=0; col < N; col++) {
                if (map[row][col].equals("1") && visited[row][col] == false) {
                    result.add(bfs(row, col));
                }
            }
        }
        System.out.println(result.size());
        result.sort(null);
        result.forEach(r -> System.out.println(r));
    }

    private static int bfs(int r, int c) {
        visited[r][c] = true;
        Deque<Loc> dq = new ArrayDeque<>();
        dq.addLast(new Loc(r, c));
        int count = 0;
        while(!dq.isEmpty()) {
            Loc current = dq.pollFirst();
            count++;
            int[][] derList = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
            for(var der : derList) {
                int newRow = current.row+der[0];
                int newCol = current.col+der[1];
                if ((0 <= newRow && newRow < N) && (0 <= newCol && newCol < N)) {
                    if (visited[newRow][newCol] == false && map[newRow][newCol].equals("1")) {
                        visited[newRow][newCol] = true;
                        dq.addLast(new Loc(newRow, newCol));
                    }
                }
            }
        }

        return count;
    }

    static class Loc {
        int row;
        int col;
        public Loc(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
}
