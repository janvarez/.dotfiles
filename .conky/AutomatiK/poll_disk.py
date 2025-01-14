import time, os

#  /dev/sda1


#Partition_Liste_Partitions_T0 = os.popen(DiskSearchCommand).read().split() # 
#print (Partition_Liste_Partitions_T0)





def Get_Disk_List():
	DiskSearchCommand="df -Th 2>/dev/null | grep -E 'dev|media' | grep -E -v '^.*(tmp|proc|sys|var|pts|daemon|root|gvfs|efi|snap|.Private).*$'"
	Liste_Partitions = os.popen(DiskSearchCommand).read().split() 
	return (Liste_Partitions)

G_Liste_Partitions=Get_Disk_List()


def job():
	global G_Liste_Partitions
	L_Liste_Partitions=Get_Disk_List()
	#print (L_Liste_Partitions)
	if L_Liste_Partitions != G_Liste_Partitions:
		os.system("python3 disk.py")
		os.system("conky -q -c diskfile")
		G_Liste_Partitions = L_Liste_Partitions

	#Partition_NameActuel=os.popen(DiskSearchCommand).read().split() # 
	#Partition_NameActuel=os.popen(DiskSearchCommand).read().split()
	#print (Partition_NameActuel)
	#os.system("python3 disk01.py")
	#if Partition_NameActuel!= Partition_Liste_Partitions_T0:
	#	os.system("python disk01.py")
		#print Partition_NameActuel
	#Partition_Liste_Partitions_T0=os.popen(DiskSearchCommand).read().split() # 


if __name__ == '__main__':
    while True:
        job()
        time.sleep(4)
