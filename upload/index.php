<?php
// Specify the path to the index.php file
$file_path = 'index.php';

// Check if the file exists
if (file_exists($file_path)) {
    // Get the contents of the file
    $file_contents = file_get_contents($file_path);
    
    // Print the contents of the file
    echo nl2br(htmlspecialchars($file_contents));
} else {
    echo "File not found.";
}
?>