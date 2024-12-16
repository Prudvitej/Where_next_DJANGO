<?php
        $insertconf = false;
        if (isset($_POST['name'])){
        $server="localhost";
        $user="root";
        $password="";
        $dbname="travel";
        
        $con = mysqli_connect($server,$user,$password,$dbname);
        
        if(!$con){
            die("Connection with database not happening due to". mysqli_connect_error());
        }
        $name =$_POST['name'];
        $email =$_POST['email'];
        $mobile =$_POST['mobile'];
        $from =$_POST['from'];
        $to =$_POST['to'];
        $date =$_POST['date'];
        $members =$_POST['members'];

        $sql_query = "INSERT INTO `travel` (`Name`, `Mobile`, `email`, `From`, `To`, `Date`, `Members`) VALUES ('$name', '$email', '$mobile', '$from', '$to', '$date', '$members');";

        if ($con->query($sql_query) ==true){
            $insertconf=true;
            echo "<h1 align='center'>Thank you for submiting............ <br> our team will contact You Soon &#128519;</h1><br><br><br> <h3 align='center'><a href='index.html'>Back to Where next</a></h3>";
           
        }else{
            echo "ERROR : $sql_query <br> $con->error";
        }
        $con->close();
        }

    ?>
