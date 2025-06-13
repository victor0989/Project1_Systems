with Ada.Numerics.Float_Random;

package body Sensors is

   function Read_Accelerometer return Vector3D is
      Gen : Ada.Numerics.Float_Random.Generator;
      V : Vector3D;
   begin
      Ada.Numerics.Float_Random.Reset(Gen);
      V.X := Ada.Numerics.Float_Random.Random(Gen) * 0.1 - 0.05;
      V.Y := Ada.Numerics.Float_Random.Random(Gen) * 0.1 - 0.05;
      V.Z := Ada.Numerics.Float_Random.Random(Gen) * 0.1 - 0.05;
      return V;
   end Read_Accelerometer;

end Sensors;



