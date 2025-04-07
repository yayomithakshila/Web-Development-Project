<?php
// Simulated KOT orders (In practice, this would be pulled from a database)
$kot_orders = [
    101 => ['item' => 'Fried Rice', 'qty' => 2],
    102 => ['item' => 'Chicken Curry', 'qty' => 1],
    103 => ['item' => 'Paneer Tikka', 'qty' => 3],
];

// Correction logic
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $kot_id = $_POST['kot_id'];
    $new_item = $_POST['item'];
    $new_qty = $_POST['qty'];

    // Normally this would update the database
    if (isset($kot_orders[$kot_id])) {
        $kot_orders[$kot_id]['item'] = $new_item;
        $kot_orders[$kot_id]['qty'] = $new_qty;
        $message = "KOT #$kot_id updated successfully.";
    } else {
        $message = "KOT ID not found.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>KOT Order Correction</title>
</head>
<body>
    <h2>Current KOT Orders</h2>
    <ul>
        <?php foreach ($kot_orders as $id => $order): ?>
            <li><strong>KOT #<?= $id ?></strong>: <?= $order['item'] ?> (Qty: <?= $order['qty'] ?>)</li>
        <?php endforeach; ?>
    </ul>

    <h3>Correct a KOT Order</h3>
    <?php if (isset($message)) echo "<p style='color: green;'>$message</p>"; ?>

    <form method="POST">
        <label for="kot_id">KOT ID:</label>
        <input type="number" name="kot_id" required><br><br>

        <label for="item">Correct Item Name:</label>
        <input type="text" name="item" required><br><br>

        <label for="qty">Correct Quantity:</label>
        <input type="number" name="qty" min="1" required><br><br>

        <input type="submit" value="Update KOT">
    </form>
</body>
</html>
