conn= new Mongo();
db= conn.getDB("symmetrybaza"); // add database name here or replace with symmetrybaza
var file= cat('LT_db_M1_2012_11_19.txt') //use diffrent txt file to manimulate it
var file2=file.slice(11);
var array= file2.split(/(\s+)/);
print(array.length);
var col=[];	 
	var name=[];	 
	var broj=[];
	var lenght0
for(var i=0;i<(array.length-10);)
{
	
	 col=[];	 
	 name=[];
	 broj=[];
	do{
		
		  col.push(array[i]);
		
		  name.push(array[i+4]);
		
		  broj.push(array[i+8]);
		i=i+10;
		
	}while(array[i]==array[i+10]);
	col.push(array[i]);
	name.push(array[i+4]);
	broj.push(array[i+8]);
	
	lenght0= col[0].length;
	print([lenght0]);
db["things"].insert({"name":col[0],[name[0].substring(lenght0+1)] : broj[0]
,[name[1].substring(lenght0+1)] : broj[1]
,[name[2].substring(lenght0+1)] : broj[2]
,[name[3].substring(lenght0+1)] : broj[3]
,[name[4].substring(lenght0+1)] : broj[4],"telescope":"M1" //if there is more fields in database add [name[5].substring(lenght0+1)] : broj[5] and more if needed
 });


i=i+10;
}
/