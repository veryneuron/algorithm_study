package baekjoon;
import java.util.*;
import java.io.*;

// 13549
// 질문 참고

public class hideAndSeek3 {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int MAX_VALUE = 100001;

        Deque<Position> dq = new ArrayDeque<>();
        dq.addLast(new Position(N, 0));
        int[] visited = new int[MAX_VALUE];
        Arrays.fill(visited, -1);
        visited[N] = 0;
        int answer = MAX_VALUE;

        while (!dq.isEmpty()) {
            Position now = dq.pollFirst();
            if (now.loc == K) {
                if (answer > now.time) {
                    answer = now.time;
                }
                continue;
            }

            if (now.loc+1 < MAX_VALUE && (visited[now.loc+1] == -1 || visited[now.loc+1] > now.time+1)) {
                visited[now.loc+1] = now.time+1;
                dq.addLast(new Position(now.loc+1, now.time+1));
            }
            if (0 <= now.loc-1 && (visited[now.loc-1] == -1 || visited[now.loc-1] > now.time+1)) {
                visited[now.loc-1] = now.time+1;
                dq.addLast(new Position(now.loc-1, now.time+1));
            }
            if (now.loc*2 < MAX_VALUE && (visited[now.loc*2] == -1 || visited[now.loc*2] > now.time)) {
                visited[now.loc*2] = now.time;
                dq.addLast(new Position(now.loc*2, now.time));
            }
        }

        System.out.println(answer);
    }

    static class Position {
        int loc;
        int time;
        Position (int l, int t) {
            this.loc = l;
            this.time = t;
        }
    }
}