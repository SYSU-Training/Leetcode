#include <iostream>

int n=8;

using namespace std;

int main(){

	int a[n]={5,1,2,0,4,6,0,9};

	int* bubble_sort(int a[]);

        int *b=bubble_sort(a);

	int *insertion_sort(int a[]);

	b=insertion_sort(a);

	int* selection_sort(int a[]);

	b=selection_sort(a);

	int *merge_sort(int a[]);

	b=merge_sort(a);

}

int* bubble_sort(int a[]){

	cout<<"Bubble Sort:"<<endl;

	int *b=new int[n];

	for(int i=0;i<n;i++) b[i]=a[i];

	for(int i=0;i<n;i++){

		for(int j=0;j+1<n-i;j++) {

			if(b[j]>b[j+1]) 

				swap(b[j],b[j+1]);

		}

		cout<<"round "<<i+1<<" :";

		for(int k=0;k<n;k++) cout<<b[k]<<" ";

		cout<<endl;

	}

	cout<<"original array:"<<endl;

	for(int i=0;i<n;i++) cout<<a[i]<<" ";

	cout<<endl;

	cout<<"sorted array:"<<endl;

	for(int i=0;i<n;i++) cout<<b[i]<<" ";

	cout<<endl;

	return b;

}

int* insertion_sort(int a[]){

	cout<<"Insertion Sort:"<<endl;

	int* b=new int[n];

	for(int i=0;i<n;i++) b[i]=a[i];

	for(int i=1;i<n;i++){

		for(int j=i;j>0;j--){

			if(b[j]<b[j-1]) swap(b[j],b[j-1]);

			else break;

		}

		cout<<"round "<<i+1<<" :";

		for(int k=0;k<n;k++) cout<<b[k]<<" ";

		cout<<endl;

	}

	cout<<"original array:"<<endl;

	for(int i=0;i<n;i++) cout<<a[i]<<" ";

	cout<<endl;

	cout<<"sorted array:"<<endl;

	for(int i=0;i<n;i++) cout<<b[i]<<" ";

	cout<<endl;

	return b;

}

int* selection_sort(int a[]){

	cout<<"Selection Sort:"<<endl;

	int* b=new int[n];

	for(int i=0;i<n;i++) b[i]=a[i];

	for(int i=0;i<n-1;i++){

		int min=i;

		for(int j=i+1;j<n;j++){

			if(b[j]<b[min]) min=j;

		}

		swap(b[min],b[i]);

		cout<<"round "<<i+1<<" :";

		for(int k=0;k<n;k++) cout<<b[k]<<" ";

		cout<<endl;

	}

	cout<<"original array:"<<endl;

	for(int i=0;i<n;i++) cout<<a[i]<<" ";

	cout<<endl;

	cout<<"sorted array:"<<endl;

	for(int i=0;i<n;i++) cout<<b[i]<<" ";

	cout<<endl;

	return b;

}

int* merge_sort(int a[]){

	cout<<"Merge Sort:"<<endl;

	int* b=new int[n];

	for(int i=0;i<n;i++) b[i]=a[i];

	void merge(int a[],int first,int mid,int last,int temp[]);

	void mergesort(int a[],int first,int last,int temp[]);

	mergesort(a,0,n-1,b);	

	cout<<"original array:"<<endl;

	for(int i=0;i<n;i++) cout<<a[i]<<" ";

	cout<<endl;

	cout<<"sorted array:"<<endl;

	for(int i=0;i<n;i++) cout<<b[i]<<" ";

	cout<<endl;

	return b;

}

void merge(int a[],int first,int mid,int last,int temp[]){

	int i=first,j=mid+1;

	int k=0;

	while(i<=mid&&j<=last){

		if (a[i]<=a[j]) temp[k++]=a[i++];

		else temp[k++]=a[j++];

	}

	while(i<=mid) temp[k++]=a[i++];

	while(j<=last) temp[k++]=a[j++];

	for(i=0;i<k;i++) a[first+i]=temp[i];

	for(int i=0;i<n;i++) cout<<a[i]<<" ";

	cout<<endl;

}

void mergesort(int a[],int first,int last,int temp[]){

    	if(first<last){

        int mid=(first+last)/2;

        mergesort(a,first,mid,temp);

        mergesort(a,mid+1,last,temp);

        merge(a,first,mid,last,temp);

    	}



}
