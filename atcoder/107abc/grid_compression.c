#include<stdio.h>
#include<string.h>
int main(){
        int H,W,i,j,k,cnt;
        char c;
        scanf("%d %d",&H,&W);
        char a[101][101];
        int b[101];
        while((c=getchar())!=EOF){
                if(strcmp(&c,"\n")==0){
                        i++;
                        j=0;
                        continue;
                }
                a[i][j]=c;
                i++;
        }
        k=0;
/*        for(i=0;i<H;i++){
                cnt=0;
                while((strcmp(".",a[i][cnt])==0)&&cnt<=W){
                        cnt++;
                        if(cnt==W)
                                b[k++]=i;
                }
        }*/
        k=0;
        for(i=0;i<H;i++){
/*                if(i==b[k]){
                        k++;
                        continue;
                }
 */               for(j=0;j<W;j++)
                        printf("%c",a[i][j]);
                printf("\n");
        }
        
}

