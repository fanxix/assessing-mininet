"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""

from mininet.topo import Topo

class GeneratedTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def __init__( self ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self )
        CHE = self.addSwitch( 's0' )
        LEI = self.addSwitch( 's1' )
        ADH = self.addSwitch( 's2' )
        DRE = self.addSwitch( 's3' )
        GSI = self.addSwitch( 's4' )
        HEI = self.addSwitch( 's5' )
        JEN = self.addSwitch( 's6' )
        ILM = self.addSwitch( 's7' )
        DeCix = self.addSwitch( 's8' )
        Geant = self.addSwitch( 's9' )
        FZK = self.addSwitch( 's10' )
        STU = self.addSwitch( 's11' )
        DeCix = self.addSwitch( 's12' )
        Telia = self.addSwitch( 's13' )
        BIE = self.addSwitch( 's14' )
        Telekom = self.addSwitch( 's15' )
        GOE = self.addSwitch( 's16' )
        BRE = self.addSwitch( 's17' )
        WUP = self.addSwitch( 's18' )
        BIR = self.addSwitch( 's19' )
        BON = self.addSwitch( 's20' )
        MAR = self.addSwitch( 's21' )
        GIE = self.addSwitch( 's22' )
        KAS = self.addSwitch( 's23' )
        PAD = self.addSwitch( 's24' )
        EWE = self.addSwitch( 's25' )
        Telekom = self.addSwitch( 's26' )
        MUE = self.addSwitch( 's27' )
        SAA = self.addSwitch( 's28' )
        GC = self.addSwitch( 's29' )
        DES = self.addSwitch( 's30' )
        HAM = self.addSwitch( 's31' )
        KIE = self.addSwitch( 's32' )
        ROS = self.addSwitch( 's33' )
        MAG = self.addSwitch( 's34' )
        BRA = self.addSwitch( 's35' )
        KAI = self.addSwitch( 's36' )
        GRE = self.addSwitch( 's37' )
        DOR = self.addSwitch( 's38' )
        BOC = self.addSwitch( 's39' )
        FHM = self.addSwitch( 's40' )
        REG = self.addSwitch( 's41' )
        AUG = self.addSwitch( 's42' )
        GAR = self.addSwitch( 's43' )
        DUI = self.addSwitch( 's44' )
        FZJ = self.addSwitch( 's45' )
        AAC = self.addSwitch( 's46' )
        WUE = self.addSwitch( 's47' )
        TUB = self.addSwitch( 's48' )
        HUB = self.addSwitch( 's49' )
        HAN = self.addSwitch( 's50' )
        FRA = self.addSwitch( 's51' )
        POT = self.addSwitch( 's52' )
        ERL = self.addSwitch( 's53' )
        BAY = self.addSwitch( 's54' )
        FFO = self.addSwitch( 's55' )
        ZIB = self.addSwitch( 's56' )
        ZEU = self.addSwitch( 's57' )

        #HOSTS (put here if needed)
        # dont forget to add edges afterwards!
        HAM_h = self.addHost( 'h1' )
        GAR_h = self.addHost( 'h2' )

        self.addLink( HAM , HAM_h )
        self.addLink( GAR , GAR_h )


        # EDD EDGES
        self.addLink( CHE , LEI)
        self.addLink( CHE , DRE)
        self.addLink( LEI , ERL)
        self.addLink( LEI , JEN)
        self.addLink( LEI , Telekom)
        self.addLink( ADH , ZIB)
        self.addLink( ADH , HUB)
        self.addLink( DRE , POT)
        self.addLink( DRE , ERL)
        self.addLink( GSI , FRA)
        self.addLink( GSI , HEI)
        self.addLink( HEI , FZK)
        self.addLink( JEN , ILM)
        self.addLink( ILM , ERL)
        self.addLink( DeCix , FRA)
        self.addLink( Geant , FRA)
        self.addLink( FZK , STU)
        self.addLink( FZK , FRA)
        self.addLink( FZK , KAI)
        self.addLink( STU , GAR)
        self.addLink( DeCix , POT)
        self.addLink( Telia , POT)
        self.addLink( BIE , PAD)
        self.addLink( BIE , HAN)
        self.addLink( BIE , MUE)
        self.addLink( GOE , HAN)
        self.addLink( GOE , KAS)
        self.addLink( BRE , EWE)
        self.addLink( BRE , HAN)
        self.addLink( BRE , HAM)
        self.addLink( WUP , BIR)
        self.addLink( WUP , DOR)
        self.addLink( BIR , FRA)
        self.addLink( BIR , BON)
        self.addLink( BON , AAC)
        self.addLink( MAR , GIE)
        self.addLink( MAR , KAS)
        self.addLink( GIE , FRA)
        self.addLink( KAS , PAD)
        self.addLink( EWE , MUE)
        self.addLink( Telekom , HAN)
        self.addLink( MUE , DUI)
        self.addLink( SAA , FRA)
        self.addLink( SAA , KAI)
        self.addLink( GC , FRA)
        self.addLink( DES , TUB)
        self.addLink( DES , HAM)
        self.addLink( KIE , ROS)
        self.addLink( KIE , HAN)
        self.addLink( ROS , HAN)
        self.addLink( ROS , GRE)
        self.addLink( MAG , BRA)
        self.addLink( MAG , POT)
        self.addLink( BRA , HAN)
        self.addLink( KAI , FRA)
        self.addLink( GRE , POT)
        self.addLink( DOR , BOC)
        self.addLink( BOC , DUI)
        self.addLink( FHM , REG)
        self.addLink( FHM , GAR)
        self.addLink( REG , ERL)
        self.addLink( AUG , GAR)
        self.addLink( AUG , ERL)
        self.addLink( GAR , FRA)
        self.addLink( DUI , HAN)
        self.addLink( DUI , FZJ)
        self.addLink( FZJ , AAC)
        self.addLink( AAC , FRA)
        self.addLink( WUE , FRA)
        self.addLink( WUE , ERL)
        self.addLink( TUB , ZIB)
        self.addLink( TUB , HUB)
        self.addLink( TUB , POT)
        self.addLink( TUB , ZEU)
        self.addLink( HAN , FRA)
        self.addLink( HAN , POT)
        self.addLink( HAN , ERL)
        self.addLink( HAN , FFO)
        self.addLink( FRA , POT)
        self.addLink( FRA , ERL)
        self.addLink( POT , ERL)
        self.addLink( POT , BAY)
        self.addLink( POT , FFO)
        self.addLink( POT , ZIB)
        self.addLink( ERL , BAY)
        self.addLink( FFO , ZIB)
        self.addLink( ZIB , ZEU)


topos = { 'generated': ( lambda: GeneratedTopo() ) }
