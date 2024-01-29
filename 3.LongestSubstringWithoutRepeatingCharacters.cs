public class Solution {
    public int LengthOfLongestSubstring(string s)
    {
        int count = 0;
        int result = 0;
        int idx = 0;
        int idx_checkpoint = 0;
    
        List<char> seen = new List<char>();
    
        while (idx < s.Length)
        {
            if (seen.Contains(s[idx]))
            {
                idx = TraceBackToDuplicate(s, seen, idx);

                if (count > result)
                {
                    result = count;
                }

                count = 1;
            }

            idx++;
            count++;
            seen.Add(s[idx]);
        }

        if (count > result)
        {
            result = count;
        }

        return result;
    }

    public int TraceBackToDuplicate(string s, List<char> seen, int idx)
    {
        /* Can use this while because we only call
           this function when we find a duplicate
           thus it will always stop */
        while (true)
        {
            if (seen.Contains(s[idx]))
            {
                return idx + 1;
            }
            seen.Remove(s[idx]);
            idx--;
        }
    }
}