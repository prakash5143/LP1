public class HillClimbing
{
    public static int cost(int[] arr)
    {
        int c=0;
        for(int i=0;i<arr.length-1;i++)
        {
            for(int j=i+1;j<arr.length;j++)
            {
                if(arr[j]<arr[i])
                    c++;
            }
        }
        return c;
    }
    
    public static void swap(int[] arr, int i,int j)
    {
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    
    public static void main(String[] args) 
    {
        int arr[]={10,5,15,12,30};
        int c=cost(arr);
        while(c>0)
        {
            for(int i=0;i<arr.length-1;i++)
            {
                swap(arr,i,i+1);
                 int c1=cost(arr);
                 if(c1<c)
                 {
                     c=c1;
                 }
                 else
                 {
                     swap(arr,i,i+1);
                 }
            }
        }
        
        for(int a : arr)
        {
            System.out.print(a+" ");
        }
    }
}