typedef long long ll;

class Solution {
    ll MOD = 1e9 + 9;
    ll base = 131;
    vector<ll> h,p;

    ll getHash(int l, int r){
        ll res = (h[r+1] - h[l] * p[r - l + 1]) % MOD;
        return (res + MOD) % MOD;
    }
public:
    long long sumScores(string s) {
        int n = s.size();
        h.assign(n+1,0);
        p.assign(n+1,1);

        for (int i = 0; i < n; i++){
            h[i+1] = (h[i] * base + (s[i]-'a' + 1)) % MOD;
            p[i+1] = (p[i]*base) % MOD;
        }

        ll totalSum = 0;
        for (int i = 0; i < n; i++) {
            int low = 1, high = n - i;
            int lcp = 0;

            // 3. Binary Search for the longest common prefix length
            while (low <= high) {
                int mid = low + (high - low) / 2;
                
                // Compare prefix of length 'mid' with suffix starting at 'i'
                if (getHash(0, mid - 1) == getHash(i, i + mid - 1)) {
                    lcp = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            totalSum += lcp;
        }

        return totalSum;

    }
};