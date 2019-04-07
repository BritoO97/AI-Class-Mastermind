{
	if ($2 < 260)
	{
		dist[1] += 1
	}
	else if ($2 < 520)
	{
		dist[2] += 1
	}
	else if ($2 < 780)
	{
		dist[3] += 1
	}
	else if ($2 < 1040)
	{
		dist[4] += 1
	}
	else if ($2 < 1297)
	{
		dist[5] += 1
	}	
}

END {print dist[1], dist[2], dist[3], dist[4], dist[5]}
