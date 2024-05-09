-- This script creates a trigger that automatically decreases the item quantity in the 'item' table
-- whenever a new order is inserted into the 'orders' table.

DELIMITER $$

CREATE TRIGGER AfterOrderInsert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.order_quantity
	WHERE item_id = NEW.item_id;
END$$

DELIMITER ;
