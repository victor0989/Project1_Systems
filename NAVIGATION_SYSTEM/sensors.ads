package Sensors is
   type Vector3D is record
      X, Y, Z : Float;
   end record;

   function Read_Accelerometer return Vector3D;
end Sensors;
