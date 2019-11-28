wvec = c(0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23)
res = matrix(nrow = 7, ncol = 7)

optimalBST <- function(wvec) {
        n = length(wvec)
        res = matrix(nrow = n, ncol = n)
        for (s in 0:n-1) {
                for (i in 1:n) {
                        sss = NULL
                        i_s = min(s+i, n)
                        for (r in i:i_s) {
                                fir = sum(wvec[i:i_s])
                                sec = ifelse(i <= r-1, res[i, r-1], 0)
                                thi = ifelse(r + 1 <= i_s, res[r+1, i_s], 0)
                                sss = c(sss, fir + sec + thi)
                        }
                        if (i+s <= n) { res[i, i + s] = min(sss)}
                }
        }
        return(res[1, n])
        
}
optimalBST(wvec)

for (s in 0:6) {
        for (i in 1:7) {
                sss = NULL
                for (r in i:min(s+i, 7)) {
                        fir = sum(wvec[i:min(s+i, 7)])
                        sec = ifelse(i <= r-1, res[i, r-1], 0)
                        thi = ifelse(r + 1 <= min(i+s, 7), res[r+1, min(i+s, 7)], 0)
                        sss = c(sss, fir +sec+thi)
                }
                if (i+s <= 7) { res[i, i +s] = min(sss)}
               
        }
}
        
                
