int lengthOfLongestSubstring(const char* str) {
    int last_idx[256] = {0};
    int start = 0, end = 0;
    int longestStart = 0, longestEnd = 0;
    int i;
    memset(last_idx, -1, 256*sizeof(int));

    for(i=0; str[i] != 0; ++i)
    {
        int c = str[i];
        if (last_idx[c] < start)
        {
            end = i+1;
        }
        else
        {
            start = last_idx[c]+1;
            end = i+1;
        }
        last_idx[c] = i;
        if (end - start > longestEnd - longestStart)
        {
            longestEnd = end;
            longestStart = start;
        }
    }
    return longestEnd-longestStart;
}
