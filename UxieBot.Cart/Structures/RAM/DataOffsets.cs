using System;

namespace UxieBot.Cart
{
    public static class DataOffsets
    {
        public const uint BoxStartOffset = 0x45075880;
        public const uint CurrentBoxOffset = 0x450C680E;
        public const uint TrainerDataOffset = 0x45068F18;
        public const uint SoftBanUnixTimespanOffset = 0x450C89E8;
        public const uint IsConnectedOffset = 0x30c7cca8;
        public const uint TextSpeedOffset = 0x450690A0;
        public const uint ItemTreasureAddress = 0x45068970;

        // 0 when not in a battle or raid, 0x40 or 0x41 otherwise.
        public const uint InBattleRaidOffsetSW = 0x3F128624;
        public const uint InBattleRaidOffsetSH = 0x3F128626;

        public const int BoxFormatSlotSize = 0x158;
        public const int TrainerDataLength = 0x110;

        #region ScreenDetection
        // CurrentScreenOffset can be unreliable for Overworld; this one is 1 on Overworld and 0 otherwise.
        // Varies based on console language which is configured in Hub.
        // Default setting works for English, Dutch, Portuguese, and Russian
        public const uint OverworldOffset = 0x2F770638;
        public const uint OverworldOffsetFrench = 0x2F770828;
        public const uint OverworldOffsetGerman = 0x2F770908;
        public const uint OverworldOffsetSpanish = 0x2F7707F8;
        public const uint OverworldOffsetItalian = 0x2F7705B8;
        public const uint OverworldOffsetJapanese = 0x2F770798;
        public const uint OverworldOffsetChineseT = 0x2F76F7D8;
        public const uint OverworldOffsetChineseS = 0x2F76F838;
        public const uint OverworldOffsetKorean = 0x2F76FC38;

        // For detecting when we're on the in-battle menu. 
        public const uint BattleMenuOffset = 0x6B578EDC;

        // Original screen detection offset.
        public const uint CurrentScreenOffset = 0x6B30FA00;

        // Value goes between either of these; not game or area specific.
        public const uint CurrentScreen_Overworld1 = 0xFFFF5127;
        public const uint CurrentScreen_Overworld2 = 0xFFFFFFFF;

        public const uint CurrentScreen_Box1 = 0xFF00D59B;
        public const uint CurrentScreen_Box2 = 0xFF000000;
        public const uint CurrentScreen_Box_WaitingForOffer = 0xC800B483;
        public const uint CurrentScreen_Box_ConfirmOffer = 0xFF00B483;

        public const uint CurrentScreen_Softban = 0xFF000000;

        //public const uint CurrentScreen_YMenu = 0xFFFF7983;
        public const uint CurrentScreen_RaidParty = 0xFF1461DB;
        #endregion
    }
}
