class  duplicateZeros{
    public void duplicate(int[] arr){
        int possibleDups = 0 ;
        int arrayLength = arr.length -1;

        // first find the number of zeros to be dupicated 
        for (int left = 0 ; left <= arrayLength - possibleDups ;left ++ ){
            // count zeros
            if (arr[left] == 0){
                //edge case: we cant dupliacate the zero if we have no more space
                if (left ==  arrayLength - possibleDups){
                    //thus we just copy it without duplication
                    arr[arrayLength] = 0 ;
                    arrayLength -= 1;
                    break;
                }
                possibleDups ++;
            }
        }

        // now we start from the backwards from the last element which would be part of the array
        int last  = arrayLength - possibleDups;

        //now copy zero twice and non zero once

        for(int i =  last; i >= 0 ; i++){
            if (arr[i] == 0){
                arr[i + possibleDups] = 0;
                possibleDups --;
                arr[i + possibleDups] = 0;
            } else {
                arr[i + possibleDups] = arr[i];
            }
        }

    }
 
 }