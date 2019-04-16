{
	num[$2] += 1
	sum[$2] += $3	
}

END {
	for (i in sum)
	{
		printf("%d - %.10f\n", i, (sum[i] / num[i]))
	}
}
