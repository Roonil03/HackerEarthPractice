# Watching Video
## Description:
Assume you are watching a video on Youtube. Consider the following hypothetical model of how video buffering takes place.

The video renders **d KB** of data per second, if watched in decent quality. Since you have a 2G Net pack, the bandwidth is fluctuating and does not support smooth video buffer. Also, the data packets send by server each second are fluctuating. The browser accumulates the data packets in cache, and once it gathers at least **d KB** data, it will play one second of video and remove that data from cache. In case it does not have enough data in cache, it will pause video and wait for enough data packets to start rendering again.

Since you do not want to watch video with such breaks, you pause the video initially and wait for browser to get enough data so that you can watch video smoothly, till the end of video i.e with no breaks. Also, you don't have much time to spare, so you want to watch video as soon as possible.

There are **N** data packets in total, received at an interval of 1 second. Your browser receives **X$_i$ KB** data in **i$^{th}$** data packet. **It takes 1 second to receive 1 data packet**. Your job, now, is to decide the earliest possible time, from which you should start playing the video (i.e hit play button), so that you can enjoy it without any breaks, with decent quality.

Assume you can only play video in integral seconds of time i.e if cache has d / 2 KB data does not mean you can play 0.5 second video. Also, the total data sent by server will be an integral multiple of d.

## INPUT
The first line will contain two space separated integers, the value of **N** and **d** respectively.
Next line will contain **N** space separated integers, the **i$^{th}$** number representing the data quantity in KB received in **i$^{th}$** data packet.

## OUTPUT
Output in one line, an integer, denoting the minimum time after which you should start playing video.

## CONSTRAINTS
$1 \le N \le 10^5$
$0 \le X_i \le 10^6$
$1 \le d \le 10^6$

## Examples:
### Example 1:
**Sample Input:**
```
3 2
1 1 2
```
**Sample Output:**
```
2
```
**Explaination:**  
After 1 second, your cache will have 1 KB data which is less than d. After 2 seconds, it will have 2 KB cache data which is equal to d. If we start playing video now, we can guarantee at least 1 second of playback and now our cache will have 0 KB. After 3 seconds, again we will have 2 KB which is equal to d and hence 1 more second of video playback. Since we never ran out of data and hence never took a break at any second, this will be our answer i.e start playing video after 2 seconds.