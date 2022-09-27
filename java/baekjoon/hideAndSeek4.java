package baekjoon;
import java.util.*;
import java.io.*;
// 코드 참고
// 이전 위치를 연속적으로 저장해야 함
public class hideAndSeek4 {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int MAX_SIZE = 100001;
        int[] visited = new int[MAX_SIZE];
        Arrays.fill(visited, -1);
        Deque<Position> dq = new ArrayDeque<>();
        dq.addLast(new Position(N, 0));
        int answer = 0;
        visited[N] = N;

        while(!dq.isEmpty()) {
            Position now = dq.pollFirst();
            if (now.loc == K) {
                answer = now.time;
                break;
            }
            int[] deltaList = {now.loc+1, now.loc-1, now.loc*2}; 
            for (var delta : deltaList) {
                if (0 <= delta && delta < MAX_SIZE) {
                    if (visited[delta] == -1) {
                        visited[delta] = now.loc;
                        dq.addLast(new Position(delta, now.time+1));
                    }
                }
            }
        }
        System.out.println(answer);
        int cur = K;;
        Deque<Integer> q = new ArrayDeque<>();
        while (cur != N) {
            q.addLast(cur);
            cur = visited[cur];
        }
        q.addLast(N);
        List<String> result = new ArrayList<>();
        while (!q.isEmpty()) {
            result.add(String.valueOf(q.pollLast()));
        }
        System.out.println(String.join(" ", result));
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
