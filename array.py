
#!/bin/bash -x
read -p "enter word > "
while [[ -h $REPLY ]]; do
    echo $REPLY
    case $REPLY in 
          [A-E])   echo "is a single alphabetic character.";break ;; 
          [ABC][0-9])    echo "is A,B,or C followed by a digit."; break ;;
          ???)           echo "is three characters long."; break ;;     
          Q)     break ;;         
          Y)     continue ;;
    esac
done 
echo "the program stops."

