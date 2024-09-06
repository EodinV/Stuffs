-- traction control will seek to even out the speed of the wheels without cutting engine power, 
dofile ("E:/SteamLibrary/steamapps/common/BeamNG.drive/lua/vehicle/controller/4wd.lua")
dofile ("E:/SteamLibrary/steamapps/common/BeamNG.drive/lua/vehicle/controller/vehicleController.lua")

function GetWheelSpeeds()
    local vehicle = be:getPlayerVehicle() -- presumably gets player vehicle
    Speed = VehicleData.airSpeed
    
    Front_left = vehicleData.wheelAccess.frontLeft.wheelSpeed
    Front_right = vehicleData.wheelAccess.frontRight.wheelSpeed
    Rear_left = vehicleData.wheelAccess.RearLeft.wheelSpeed
    Rear_right = vehicleData.wheelAccess.RearRight.wheelSpeed

    
end

function Averages()
    Full_average = (Front_left + Front_right + Rear_left + Rear_right) / 4
    Front_average = (Front_left + Front_right) / 2
    Rear_average = (Rear_left + Rear_right) / 2
    Velocity_average = (Speed + Full_average) / 2
end

-- faster wheel is slipping, calculating percentage of slip
function TractionDiffLR(Left, Right) 
    TracdiffL = 0
    TracDiffR = 0
    if Left > Right then
        local TracDiffLR = Right / Left * 100
        if TracDiffLR >= 100 then
            TracDiffR = 100
        else TracDiffR = Right / Left * 100
        end
    end
    if Right > Left then
        local TracDiffLR = Left / Right * 100
        if TracDiffLR <= 0 then
            TracDiffL = 0
        else TracDiffL = Left / Right * 100
        end
    end
end

function TractionDiffFB(Front, Back) 
    if Front > Back then
        local TracDiffFB = Back / Front * 100
        if TracDiffFB >= 100 then
            TracDiffB = 100
        else TracDiffB = Back / Front * 100
        end
    end
    if Back > Front then
        local TracDiffFB = Front / Back * 100
        if TracDiffFB <= 0 then
            TracDiffF = 0
        else TracDiffF = Front / Back * 100
        end
    end
end

function TractionCheck()
    GetWheelSpeeds()
    Averages()

    if Full_average > Speed then
        Slipping = true
        SlippingWB = 0
    end
    if Slipping and Front_average > Rear_average then
        SlippingWB = 1
    end
    if Slipping and Rear_average > Front_average then
        SlippingWB = 2    
    end
    if SlippingWB == 1 then
        TractionDiffLR(Front_left, Front_right)
        TractionDiffFB(Front_average, Rear_average)
    end
    if SlippingWB == 2 then
        TractionDiffLR(Rear_left, Rear_right)
        TractionDiffFB(Front_average, Rear_average)
    end
end

function TractionControl()
    TractionCheck()
    -- apply brakes with same percentage as TractionDiff or an amalgamation of The Diffs applicable, 
    -- if slip is not mitigated within ,05 to ,5 seconds Lock diffs if possible. only lock diff on 
    -- axle with most slip and only release diff if airspeed is above 3 m/s. 
end

function Main()
    TractionControl()

end    

Main()