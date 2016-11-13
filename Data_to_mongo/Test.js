conn= new Mongo();
db= conn.getDB("Diplomski");
var file= cat('LT_db_M1_2012_11_19.txt')
var file2=file.slice(11);
var array= file2.split(/(\s+)/);
print(array.length);
for(var i=0;i<(array.length-10);)
{
var col=array[i];

var name=array[i+4];

var broj=array[i+8];
db[col].insert({"name":name,"broj":broj});
i=i+10;
}
//var name=array[i+1];
//var broj=array[i+2];
//print (col+""+name+""+broj);
//}
//db[col].insert({"name":name,"broj":broj});
//for (var i=11;i<file.search("HitFrac_Sig");i=i+41)
//{
//var col=file.slice(i+0,i+8);
//var name=file.slice(i+10,i+27);
//var broj=file.slice(i+29,i+40);
//db[col].insert({"name":name,"broj":broj});
//}
//db[col].find();