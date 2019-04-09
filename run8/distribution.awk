{
	dist[$2] += 1	
}
END {
	for (i in dist)
	{
		print i, dist[i]	
	}	
}
